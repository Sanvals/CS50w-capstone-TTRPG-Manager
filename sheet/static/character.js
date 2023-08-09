document.addEventListener('DOMContentLoaded', function() {
  // Capture data to add "+" and change the color
  const statPlus = document.querySelectorAll('.stat-bonus');
  // Capture JSON data from python
  const classSaveJson = document.querySelector('#class_save_data_json').textContent;
  const classSave = JSON.parse(classSaveJson);
  // Capture the class of the character
  const CharacterClass = character_class;
  // Capture the level of the character
  const CharacterLevel = character_level;
  // Display the proficiency bonus according to the character's level
  document.querySelector(".proficiency-bonus").innerHTML = "<span>proficiency bonus:</span>+" + (2 + Math.floor(CharacterLevel/4));

  // Display the passive perception
  document.querySelector(".passive-perception").innerHTML = "<span>passive perception:</span>+" + (wisdom_bonus + 10);

  // Change the color of the stat in which the character is proficient
  function catchSaveProficiency() {
    // Loop through the classes and check
    statPlus.forEach((stat) => {
      // Get the stat from the div
      const dataStat = stat.getAttribute('data-stat');
      // Extract the proficiencies from the python data
      const saveProficiency = classSave[CharacterClass]

      if (saveProficiency.includes(dataStat)) {
        stat.style.borderColor = "#FFD700";
      }
    });
  }

  catchSaveProficiency();


  // Catch the stats bonuses and add "+"
  statPlus.forEach((stat) =>  {
    if (!stat.textContent.includes("-")) {
      const content = stat.textContent;
      stat.textContent = `+${content}`;
      }
    });

  // Fatch the state of the inspiration boon
  const inspirationCheckbox = document.querySelector('#inspirationCheckbox');
  // Set the checkbox to the character inspiration state
  inspirationCheckbox.checked = inspiration;
  // Listen to the checkbox and send the updated data
  inspirationCheckbox.addEventListener('change', function() {
    const formData = new FormData()
    formData.append('form', 'inspiration')
    formData.append('value', 'change')
    fetch(`/update_character/${character_pk}/`, {
      method: 'POST',
      body: formData,
    })
  });


  // Capture the basic-info forms, print "-add content-"
  const editableFields = document.querySelectorAll('.editable-data')
  editableFields.forEach((element) =>{
    element.addEventListener('dblclick', editableAdd);
    element.addEventListener('blur', editableSend);

    if (["-", "", " ", "  "].includes(element.textContent)) {
      element.textContent = "-add content-";
    }
  })

  function editableAdd(event) {
    // Make the element editable
    event.target.setAttribute('contenteditable', 'true');
    event.target.focus();
  }

  function editableSend(event) {
    // Send the new data via FETCH POST request
    const editValue = event.target.textContent;
    // Fetch the ID of the form
    const editField = event.target.parentElement.dataset.field;

    // Send the edited value to python
    const formData = new FormData();
    formData.append('form', editField)
    formData.append('value', editValue)

    fetch(`/update_character/${character_pk}/`, {
      method: 'POST',
      body: formData,
    })

    event.target.removeAttribute('contenteditable');
  }
  
  // Level UP functionality, capture the Lv text
  const editLevel = document.querySelector('.editable-level');
  // Add an event listener to upgrade the emojis
  editLevel.addEventListener('dblclick', function () {
    currentLevel = parseInt(this.textContent.split(" ")[0]);

    // Check if there's ⬆️ or ✅ as a confirmation way
    if (this.textContent.includes("✅")) {
      this.textContent = String(currentLevel + 1) + " ⬆️";
      // Update the character's data
      const formData = new FormData();
      formData.append('form', 'level');
      formData.append('value', currentLevel + 1)

      fetch(`/update_character/${character_pk}/`, {
        method: 'POST',
        body: formData,
      })
    } else {
      this.textContent = String(currentLevel) + " ✅";
    }
  })

  // Add the functionality to change the current HP and the temporary HP
  // Catch the damage control text
  const scoreDamageControl = document.querySelector('#score-damage-control')
  // Catch the current HP text
  const currentDamage = document.querySelector('#score-current-HP')
  // Catch the temporary HP
  const temporaryHP = document.querySelector('#score-temporary-HP')
  // Catch the maxHP
  const maxHP = document.querySelector('#score-max-HP')

  scoreDamageControl.addEventListener('dblclick', editableAdd)
  scoreDamageControl.addEventListener('blur', function() {
    const score = parseInt(this.textContent);
    const current = parseInt(currentDamage.textContent);
    const temporary = parseInt(temporaryHP.textContent);
    const maximum = parseInt(maxHP.textContent)
    const cardImage = document.querySelector('#card-src-image')

    // On damage received
    if (score < 0) {
      // First consume the temporary
      if (score + temporary > 0) {
        temporaryHP.textContent = score + temporary;

      } else {
        // Then consume the current
        if (score + temporary + current > 0){
        currentDamage.textContent = score + (temporary + current);
        temporaryHP.textContent = 0;

        // Update the current HP
        formData = new FormData()
        formData.append('form', "currentHP")
        formData.append('value', score + (temporary + current))
    
        fetch(`/update_character/${character_pk}/`, {
          method: 'POST',
          body: formData,
        })

        } else {
          temporaryHP.textContent = 0;
          currentDamage.textContent = 0;
          cardImage.classList.add("filter");

          // Update the current HP
          formData = new FormData()
          formData.append('form', "currentHP")
          formData.append('value', 0)
      
          fetch(`/update_character/${character_pk}/`, {
            method: 'POST',
            body: formData,
          })

        }
      }
    } else {
      cardImage.classList.remove("filter");
      // Take the healing approach
      // Do not heal more than the max
      if ((score + current) > maximum) {
        currentDamage.textContent = maximum;

        // Update the currentHP
        formData = new FormData()
        formData.append('form', "currentHP")
        formData.append('value', maximum)
    
        fetch(`/update_character/${character_pk}/`, {
          method: 'POST',
          body: formData,
        })

      } else {
        currentDamage.textContent = current + score;

        // Update the currentHP
        formData = new FormData()
        formData.append('form', "currentHP")
        formData.append('value', current + score)
    
        fetch(`/update_character/${character_pk}/`, {
          method: 'POST',
          body: formData,
        })
      }
    }
    // Return this cell to 0
    this.textContent = 0;

  })
  // Allow the user to modify the temporaryHP
  temporaryHP.addEventListener('dblclick', editableAdd)

  // Allow the user to modify the MaxHP
  maxHP.addEventListener('dblclick', editableAdd)
  maxHP.addEventListener('blur', function () {
    newMaxHP = parseInt(this.textContent)

    formData = new FormData()
    formData.append('form', "newMaxHP")
    formData.append('value', newMaxHP)

    fetch(`/update_character/${character_pk}/`, {
      method: 'POST',
      body: formData,
    })

  })

  // Manage the Items and Spells buttons
  const itemsButton = document.getElementById('button-items');
  const itemsAddButton = document.getElementById('button-add-items');
  const spellsButton = document.getElementById('button-spells');
  const spellsAddButton = document.getElementById('button-add-spells');

  // Manage the areas
  const itemsArea = document.getElementById('item-part');
  const spellsArea = document.getElementById('spell-part');

  // Manage the adding windows
  const addItemWindow = document.getElementById('window-add-item');
  const addSpellWindow = document.getElementById('window-add-spell');

  // Gather the databases
  const itemsDataJSON = document.querySelector('#items').textContent;
  const spellsDataJSON = document.querySelector('#spells').textContent;
  const items = JSON.parse(itemsDataJSON);
  const itemList = document.querySelector('.table-group-divider');
  const spells = JSON.parse(spellsDataJSON);
  const spellsList = document.querySelector('.table-group-divider-spells');

  // Gather the text inputs
  const itemSearch = document.getElementById('item-search');
  const spellSearch = document.getElementById('spell-search');

  // Manage the button to hide or show the "Add items" or "Spells"
  itemsButton.addEventListener('click', function () {
    itemsButton.style.display = "none"
    itemsAddButton.style.display = "block";
    itemsArea.style.display = "block";

    spellsButton.style.display="block";
    spellsAddButton.style.display="none";
    spellsArea.style.display = "none";

    addSpellWindow.style.display="none";
  })

  spellsButton.addEventListener('click', function () {
    itemsButton.style.display = "block";
    itemsAddButton.style.display = "none";
    itemsArea.style.display = "none";

    spellsButton.style.display="none";
    spellsAddButton.style.display="block";
    spellsArea.style.display = "block";

    addItemWindow.style.display="none";
  })

  // Display the window to add items
  itemsAddButton.addEventListener('click', function () {
    addItemWindow.style.display="block";
    this.style.display = "none";
  })

  // Display the window to add spells
  spellsAddButton.addEventListener('click', function () {
    addSpellWindow.style.display="block";
    this.style.display = "none";
  })


  // Form the query to show available items to add
  itemSearch.addEventListener('input', function () {
    query = itemSearch.value.toLowerCase();
    itemList.innerHTML = "";

    // Limit the search to 5 results
    let counter = 0;

    // Cycle through the database for matches
    items.forEach((element) => {
      let name = element['fields']['name'].toLowerCase();
      
      if (name.startsWith(query) && counter < 5) {
        row = document.createElement('tr');
        row.innerHTML  = 
        `
        <td><button class="add-item-btn btn btn-sm btn-success btn-search" data-pk=${element['pk']}>+</button></td>
        <td class="search-owned-item">${element['fields']['name'] || ""}</td>
        <td>${element['fields']['type'] || ""}</td>
        `
        itemList.appendChild(row);
        counter += 1;

      }      
    })

    // Configure the button to add to the character
    const addButton = document.querySelectorAll(".add-item-btn");
    addButton.forEach((button, index) => {
      button.addEventListener('click', () => {

        // Pass the data to python
        sendData("add_item", parseInt(button.dataset.pk));

        // Draw the new item to the character sheet
        const ownedItems = document.getElementById('owned-items');
        row = document.createElement('tr');
        row.innerHTML = 
        `
        <td>1</td>
        <td>${items[button.dataset.pk]['fields']['name']}</td>
        <td><button class="add-item-btn btn btn-sm btn-danger btn-delete" data-pk="${button.dataset.pk}">-</button></td>
        `

        ownedItems.appendChild(row);
      })
    })


  })

  // Manage all the delete item buttons
  const deleteButtons = document.querySelectorAll('.btn-delete');

  deleteButtons.forEach((element) => {
    element.addEventListener('click', function () {
      
      // Pass the data to python
      sendData("delete_item", element.dataset.pk)

      // Delete the closest TR tag
      element.closest("tr").style.display = "none";
    })
  })
  

  // Form the query to show available spells to add
  spellSearch.addEventListener('input', function() {
    query = spellSearch.value.toLowerCase();
    spellsList.innerHTML = "";

    // Limit the search to 5 results
    let counter = 0;

    // Cycle through the database for matches
    spells.forEach((element) => {
      let name = element['fields']['name'].toLowerCase();
      let level = element['fields']['level'];

      if (name.startsWith(query) && counter < 5) {

        row = document.createElement('tr');
        row.innerHTML  = 
        `
        <td><button class="add-spell-btn btn btn-sm btn-success btn-search" data-pk=${element['pk']}>+</button></td>
        <td class="search-owned-spell">${element['fields']['name'] || ""}</td>
        <td>${element['fields']['level'] || ""}</td>
        <td>${level}</td>
        `
        spellsList.appendChild(row);
        counter += 1;

      }      
    })

    // Configure the button to add to the character
    const addSpellButton = document.querySelectorAll(".add-spell-btn");
    addSpellButton.forEach((button, index) => {
      button.addEventListener('click', () => {
        // Send the data to python
        sendData("add_spell", parseInt(button.dataset.pk));

        // Draw the new spell to the character sheet
        const ownedSpells = document.getElementById('owned-spells');
        row = document.createElement('tr');
        row.innerHTML =
        `
        <td>${spells[button.dataset.pk]['fields']['level']}</td>
        <td>${spells[button.dataset.pk]['fields']['name']}</td>
        <td><button class="add-item-btn btn btn-sm btn-danger btn-delete-spell" data-pk="${button.dataset.pk}">-</button></td>
        `

        ownedSpells.appendChild(row);
      })
    })
  })

  const deleteSpellButtons = document.querySelectorAll('.btn-delete-spell')
  deleteSpellButtons.forEach((element) => {
    element.addEventListener('click', function () {
      // Pass the data to python
      sendData("delete_spell", element.dataset.pk)

      // Delete the closest TR tag
      element.closest("tr").style.display = "none";
    })
  })

  // Update the wealth
  goldCoins = document.getElementById('gold-coins');
  goldCoins.addEventListener('dblclick', editableAdd);
  goldCoins.addEventListener('blur', function () {
    sendData("gold-coins", goldCoins.textContent);
  });

  silverCoins = document.getElementById('silver-coins');
  silverCoins.addEventListener('dblclick', editableAdd);
  silverCoins.addEventListener('blur', function () {
    sendData("silver-coins", silverCoins.textContent);
  });

  copperCoins = document.getElementById('copper-coins');
  copperCoins.addEventListener('dblclick', editableAdd);
  copperCoins.addEventListener('blur', function () {
    sendData("copper-coins", copperCoins.textContent);
  });

  // Manage the temporary inventory
  const creationItems = document.querySelector('#creation-items');
    if (creationItems) {
    const tempInventoryJson = document.querySelector('#temp_inventory').textContent;
    const tempInventory = JSON.parse(tempInventoryJson);
    tempInventory.forEach((element) => {
      row = document.createElement('li');
      row.innerHTML =
      `
      <li>${element}</li>
      `
      creationItems.appendChild(row);
    })

    // Delete the temporary inventory
    const deleteTemporaryInventoryButton = document.querySelector('.btn-delete-temporary');
    deleteTemporaryInventoryButton.addEventListener('click', function () {
      sendData("del_temporary", "");

      this.parentElement.style.display= "none";
    })
  }
});

function sendData(form, value) {
  formData = new FormData()
  formData.append('form', form);
  formData.append('value', value);
  
  fetch(`/update_character/${character_pk}/`, {
    method: 'POST',
    body: formData,
  })
}