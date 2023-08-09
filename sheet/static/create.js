document.addEventListener('DOMContentLoaded', function() {
  // Catch the value on the class choice
  const classChoiceField = document.querySelector('#id_class_choice');

    // Catch the different stat-forms
    const statFields = {
        'strength': document.querySelector('#id_strength'),
        'dexterity': document.querySelector('#id_dexterity'),
        'constitution': document.querySelector('#id_constitution'),
        'intelligence': document.querySelector('#id_intelligence'),
        'wisdom': document.querySelector('#id_wisdom'),
        'charisma': document.querySelector('#id_charisma'),
    };

    // -- RECOMMEND STATS ALLOCATION TO THE USER -- //

    // Catch the randomly generated stats from Python via DOM
    const initialDataJson = document.querySelector('#initial-data').textContent;
    const initialData = JSON.parse(initialDataJson);
  
    // Catch the class recomendation from Python via DOM
    const classRecommendationJson = document.querySelector('#class-recommendation-data').textContent;
    const classRecommendation = JSON.parse(classRecommendationJson);
    
    function updateStatsForClass() {
        const classSelected = classChoiceField.value
        const recommendedStats = classRecommendation[classSelected];
        const reorderedStats = {};

        // Assign the generated stats to the recommended stat order
        for (let i = 0; i < recommendedStats.length; i++) {
            reorderedStats[recommendedStats[i]] = initialData[Object.keys(initialData)[i]];
        }

        // Update the stat fields with the reordered stats
        for (const stat in statFields) {
            statFields[stat].value = reorderedStats[stat];
        }

        // Update the scores
        updateScores();
    }

    // Function to update the scores of each stat
    function updateScores() {
        for (const stat in statFields) {
            const score = calculateScore(statFields[stat].value);
            const scoreElement = document.querySelector(`#score-${stat}`);
            if (scoreElement) {
                scoreElement.textContent = `${score >= 0 ? '+' : ''}${score}`;
            }
        }
    }

    // -- DISPLAY THE STAT SAVES ACCORDING TO THE CLASS SELECTED

    // Catch the save stats from python via DOM
    const classSaveJson = document.querySelector('#class-save-data').textContent;
    const classSave = JSON.parse(classSaveJson);

    // Catch all the 'save' tags
    const saveTags = document.querySelectorAll('.save-score-tag');

    function updateStatSave() {
        // Catch the value of the classChoiceField
        const classSelected = classChoiceField.value;

        // Check for the tags, if there's a match, modify the "hidden" property
        for (const tag of saveTags) {
            const statTag = tag.getAttribute('id').split("-")[3].toLowerCase();

            if (classSave[classSelected].includes(statTag)) {
                tag.removeAttribute('hidden');
            } else {
                tag.setAttribute('hidden', true);
            }
        }
    }

    // Function to calculate the score based on the stat value
    function calculateScore(statValue) {
        return Math.floor((parseInt(statValue) - 10) / 2);
    }

    // Call the functions on page load to set initial stats and scores
    updateStatsForClass();
    updateStatSave();

    // Call the updateStatsForClass function when the class choice changes
    classChoiceField.addEventListener('change', updateStatsForClass);
    classChoiceField.addEventListener('change', updateStatSave);

    // Add event listeners to each stat input field to update the scores
    for (const stat in statFields) {
        statFields[stat].addEventListener('input', updateScores);
    }

    // Keep track that the user clicked max 4 skills
    // Catch the checkboxes
    const skillCheckboxes = document.querySelectorAll('.item-skill input[type="checkbox"]');
    const chooseSkills = document.querySelector('.skill-title')
    const maxSkills = 4; // Set the maximum number of skills the user can select
  
    // Function to update the selected skill count and disable checkboxes if limit is reached
    function updateSelectedSkills() {
      let selectedSkills = 0;
      skillCheckboxes.forEach(function(checkbox) {
        if (checkbox.checked) {
          selectedSkills++;
        }
      });
  
      if (selectedSkills >= maxSkills) {
        chooseSkills.textContent = '✅ Choose 4 skills'
        skillCheckboxes.forEach(function(checkbox) {
          if (!checkbox.checked) {
            checkbox.disabled = true;
          }
        });
      } else {
        chooseSkills.textContent = 'Choose 4 skills'
        skillCheckboxes.forEach(function(checkbox) {
          checkbox.disabled = false;
        });
      }
    }
  

    // Add event listeners to skill checkboxes to update the selected skills
    skillCheckboxes.forEach(function(checkbox) {
      checkbox.addEventListener('change', function() {
        updateSelectedSkills();
      });
    });

    // Gather the choices for every class
    const classChoicesJson = document.querySelector('#class-equipment-data').textContent;
    const classChoices = JSON.parse(classChoicesJson);

    function updateClassChoices() {
      // Extract the value on the select menu
      const classSelected = classChoiceField.value;

      // And parse the python data for the associated value
      const choices = classChoices[classSelected];

      // Generate the menu for chosing equipment
      let html = '';
      for (const key in choices) {
        // If there's not only 1 option, we draw the select inputs
        if (choices[key].length != 1) {
          // Header of the select input
          let line = 
          `
          <p>
            <div class="choices_container">
              <div class="choice_title">
                Choose:
              </div>
            <select name="${key}" class="form-select form-select-sm">
          `;

          for (let i = 0; i < choices[key].length; i++) {
            // Options of the select input
            let option = 
            `
            <option value="${choices[key][i]}">
              ${choices[key][i]}
            </option>
            `;

            // Append the option to the line
            line += option;
          }
          
          // Append the line to the HTML and close the select
          html += line;
          html += `</select></p></div>`
        } 
        
        // IF there's only one option, just send it in a hidden tag
        else {
          let line = `<p><div class="choices_container"><div class="choices_title">And:&nbsp</div>${choices[key][0]}`

          html += line;
          html += `<input type=hidden name="${key}" value="${choices[key][0]}"/>`
          html += `</p></div>`
        }
    }
    
    const show_equipment_options = document.querySelector('#class_equipment');
    show_equipment_options.innerHTML = html;
    }

    updateClassChoices();
    classChoiceField.addEventListener('change', updateClassChoices);

    // Update the info on hitdice
    // First, catch and create the variables
    const hitdice_number = document.querySelector("#card_hitdice_number");
    const hitdice_dice = document.querySelector("#card_hitdice_dice");

    // Then, cath the data parsed from python
    const hitdice_data_json = document.querySelector("#class-hitdice-data").textContent;
    const hitdice_data = JSON.parse(hitdice_data_json)

    // Create the function to update the hit dice
    function updateHitdiceDice() {
      // Extract the value on the select menu
      const classSelected = classChoiceField.value;

      // And parse the information from the json data
      const value = hitdice_data[classSelected];
      hitdice_dice.textContent = value;
    };

    // Call the function and add the event listener on class change
    updateHitdiceDice();
    classChoiceField.addEventListener('change', updateHitdiceDice);

    // And another function to update the hitdice number
    function updateHitdiceNumber() {
      const levelSelected = document.querySelector("#id_level").value;
      
      hitdice_number.textContent = levelSelected;
    }

    updateHitdiceNumber();
    levelField = document.querySelector("#id_level")
    levelField.addEventListener('change', updateHitdiceNumber)

    // Now we create a little function to generate a random dice number
    function diceRoller(n, dice) {
      total = 0;
      for (let i = 1; i < n; i++){
        roll = Math.floor(Math.random() * n + 1);
        console.log(roll);
        total += roll;
      }

      return total;
    }

    // Display random numbers for the starting gold
    const gold = diceRoller(5, 4) + 10;
    document.querySelector("#gold_amount").textContent = gold;
    document.querySelector("#coin_gold").value = gold;
  });