// Developer: Hamdy Abou El Anein
// Contact: hamdy.aea@protonmail.com
// SPDX-License-Identifier: GPL-3.0-only
'use strict';
const search=document.getElementById('search'),category=document.getElementById('category');
if(search&&category){
 const cards=[...document.querySelectorAll('#catalogue .object-card')];
 const update=()=>{
  const q=search.value.trim().toLocaleLowerCase(),k=category.value;let visible=0;
  for(const card of cards){const show=card.dataset.name.includes(q)&&(!k||card.dataset.category===k);card.hidden=!show;if(show)visible++;}
  document.getElementById('count').textContent=visible+' of '+cards.length+' objects';
  document.getElementById('no-results').hidden=visible!==0;
 };
 search.addEventListener('input',update);category.addEventListener('change',update);update();
}
