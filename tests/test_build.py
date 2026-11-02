#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# SPDX-License-Identifier: GPL-3.0-only
import json,sys,tempfile,unittest
from datetime import date
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from build import event,normalize,build
class Astrometry(unittest.TestCase):
 def test_valid_and_invalid_dates(self):
  self.assertEqual(event("2026,11,02"),date(2026,11,2))
  for s in ("2026,02,30","-33922,01,01","garbage","2026-01-01"):self.assertIsNone(event(s))
 def test_no_fabricated_events(self):
  obj=normalize({"Mars":[{"Peri":["2020,01,01"],"info":"Planet"}]},date(2026,11,2))[0]
  self.assertIsNone(obj["next"]);self.assertIsNone(obj["progress"])
 def test_elapsed_interval_only(self):
  obj=normalize({"Earth":[{"Peri":["2026,01,01","2027,01,01"]}]},date(2026,7,1))[0]
  self.assertEqual(obj["progress"],49.6)
 def test_untrusted_content_is_escaped(self):
  with tempfile.TemporaryDirectory() as temp:
   base=Path(temp);source=json.loads((Path(__file__).parents[1]/"data/orbital.json").read_text())
   source["<img src=x onerror=alert(1)>"]=[{"info":"Planet","Peri":["2026,01,01","2027,01,01"]}]
   p=base/"input.json";p.write_text(json.dumps(source));build(p,base/"site",date(2026,11,2))
   html=(base/"site/objects.html").read_text()
   self.assertNotIn("<img src=x onerror=alert(1)>",html);self.assertIn("&lt;img src=x",html)
 def test_real_dataset(self):
  src=Path(__file__).parents[1]/"data/orbital.json"
  with tempfile.TemporaryDirectory() as temp:
   build(src,Path(temp),date(2026,11,2))
   data=json.loads((Path(temp)/"data/objects.json").read_text())
   self.assertGreaterEqual(len(data["objects"]),30)
   self.assertTrue(all(0<=o["progress"]<=100 for o in data["objects"] if o["progress"] is not None))
if __name__=="__main__":unittest.main()
