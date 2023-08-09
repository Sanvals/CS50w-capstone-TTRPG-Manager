document.addEventListener('DOMContentLoaded', function() {
    // Extract the queries
    // -- For items
    const typeFilter = document.getElementById('type');
    const nameFilter = document.getElementById('name');
    const tableBody = document.querySelector('.table-group-divider');
    // -- For spells
    const classFilter = document.getElementById('class');
    const nameSpellsFilter = document.getElementById('nameSpells');
    const tableSpellsBody = document.querySelector('.table-group-divider-spells');
    const levelSpells = document.querySelector('#levelSpell');

    // Extract the buttons
    const buttonItems = document.getElementById('button-items');
    const buttonSpells = document.getElementById('button-skills');

    // Extract the databases
    const itemsDataJSON = document.querySelector('#items').textContent;
    const spellsDataJSON = document.querySelector('#spells').textContent;

    // Extract the menus
    const menuItems = document.getElementById('menu-items');
    const menuSpells = document.getElementById('menu-spells');

    // Parse the databases
    const items = JSON.parse(itemsDataJSON);
    const spells = JSON.parse(spellsDataJSON);

    // Extract the cards
    const itemCard = document.getElementById('item-card');
    const spellCard = document.getElementById('spell-card')

    // Extract the cards titles
    const itemTitle = document.getElementById('item-name');
    const itemDescription = document.getElementById('item-desc');

    // Extract the descriptions
    const spellsTitle = document.getElementById('spell-name');
    const spellsDescription = document.getElementById('spell-desc');


    // Arrange the buttons to show or hide the boxes
    buttonItems.addEventListener('click', function () {
        menuItems.style.display = "block";
        itemCard.style.display = "block";
        menuSpells.style.display = "none";
        spellCard.style.display = "none";
    });

    buttonSpells.addEventListener('click', function () {
        menuItems.style.display = "none";
        itemCard.style.display = "none";
        menuSpells.style.display = "block";
        spellCard.style.display = "block";
    });

    // listen to the input on the text box
    nameFilter.addEventListener('input', function() {
        // Save the value
        const query = nameFilter.value.toLowerCase();
        const filter = typeFilter.value.toLowerCase();
        // Create a placeholder for the search
        tableBody.innerHTML = '';
        // Loop through every element on the database for matches
        items.forEach((element) => {
            // Display the item if it parcially matches the query
            let name = element['fields']['name'].toLowerCase();
            let type = element['fields']['type'].toLowerCase();

            // Check matches
            if (name.startsWith(query) && type.includes(filter)) {
                row = document.createElement('tr');
                row.innerHTML = 
                `
                    <td>${element['fields']['name'] || "" }</td>
                    <td>${element['fields']['type'] || "" }</td>
                    <td>${element['fields']['attunement'] ? "Yes" : "No" }</td>
                    <td>${element['fields']['properties'] || "" }</td>
                    <td>${element['fields']['weight'] || "0 lb" }</td>
                    <td>${element['fields']['value'] || "0 gp" }</td>
                `;
                tableBody.appendChild(row);
                
                row.addEventListener('click', function() {
                    itemTitle.innerHTML = element['fields']['name'];
                    itemDescription.innerHTML = element['fields']['text'];
            })
            
            }

        });
    });

    // Listen to the filter on the ITEMS menu
    typeFilter.addEventListener('input', function() {
        // Save the value
        const query = nameFilter.value.toLowerCase();
        const filter = typeFilter.value.toLowerCase();
        // Create a placeholder for the search
        tableBody.innerHTML = '';
        // Loop through every element on the database for matches
        items.forEach((element) => {
            // Display the item if it parcially matches the query
            let name = element['fields']['name'].toLowerCase();
            let type = element['fields']['type'].toLowerCase();

            // Check matches
            if (name.startsWith(query) && type.includes(filter)) {
                row = document.createElement('tr');
                row.innerHTML = 
                `
                    <td>${element['fields']['name'] || "" }</td>
                    <td>${element['fields']['type'] || "" }</td>
                    <td>${element['fields']['attunement'] ? "Yes" : "No" }</td>
                    <td>${element['fields']['properties'] || "" }</td>
                    <td>${element['fields']['weight'] || "0 lb" }</td>
                    <td>${element['fields']['value'] || "0 gp" }</td>
                `;
                tableBody.appendChild(row);
            }
        });
    });

    // Listen to the input on the spell name box
    nameSpellsFilter.addEventListener('input', function() {
        // Save the value
        const query = nameSpellsFilter.value.toLowerCase();
        const classQuery = classFilter.value.toLowerCase();
        const level = levelSpells.value;
        // Create a placeholder for the search
        tableSpellsBody.innerHTML = '';
        // Loop through every element on the database for matches
        spells.forEach((element) => {
            // Display the item if it parcially matches the query
            let name = element['fields']['name'].toLowerCase();
            let classFilter = element['fields']['classes'].toLowerCase();
            let levelFilter = element['fields']['level'].toLowerCase();

            // Check matches
            if (name.startsWith(query) && classFilter.includes(classQuery) && levelFilter.includes(level)) {
                row = document.createElement('tr');
                row.innerHTML = 
                `
                    <td>${element['fields']['name'] || "" }</td>
                    <td>${element['fields']['level'] || "" }</td>
                    <td>${element['fields']['casting'] || "" }</td>
                    <td>${element['fields']['duration'] || "" }</td>
                    <td>${element['fields']['range'] || "" }</td>
                    <td>${element['fields']['components'] || "" }${element['fields']['cost'] ? "*" : ""}</td>
                    <td>${element['fields']['school'] || "" }</td>
                `;
                
                tableSpellsBody.appendChild(row);

                row.addEventListener('click', function() {
                    spellsTitle.innerHTML = element['fields']['name'];
                    spellsDescription.innerHTML = element['fields']['text'];
                })
                
            }

        });
    });
});

