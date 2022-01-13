var steam_tags = ['Indie', 'Action', 'Adventure', 'Casual', 'Simulation', 'Strategy', 'RPG', 'Singleplayer', 'Early Access', 'Free to Play', '2D', 'Atmospheric', 'Violent', 'Sports', 'Massively Multiplayer', 'Multiplayer', 'Puzzle', 'Story Rich', '3D', 'Fantasy', 'Pixel Graphics', 'Colorful', 'Racing', 'Nudity', 'Gore', 'Sexual Content', 'Exploration', 'Cute', 'Anime', 'First-Person', 'Funny', 'Sci-fi', 'Arcade', 'Shooter', 'Horror', 'Family Friendly', 'Retro', 'Great Soundtrack', 'Relaxing', 'Open World', 'Action-Adventure', 'Platformer', 'Co-op', 'Survival', 'Female Protagonist', 'Difficult', 'Combat', 'Third Person', 'VR', 'Comedy', 'Old School', 'Stylized', 'PvP', 'FPS', 'Visual Novel', 'Online Co-Op', 'Choices Matter', 'Realistic', 'Controller', 'Physics', 'Top-Down', 'Dark', 'Mystery', 'Character Customization', 'Sandbox', 'Cartoony', 'Shoot \'Em Up', 'Psychological Horror', 'Multiple Endings', 'Tactical', 'Design & Illustration', '2D Platformer', 'PvE', 'Minimalist', 'Space', 'Building', 'Utilities', 'Point & Click', 'Linear', 'Local Multiplayer', 'Futuristic', 'Management', 'Magic', 'Action RPG', '1980s', 'Crafting', 'Hand-drawn', 'Turn-Based', 'Side Scroller', 'Education', 'Replay Value', 'Procedural Generation', 'Cartoon', 'Medieval', 'Puzzle Platformer', 'Resource Management', 'Mature', 'Survival Horror', 'Zombies', 'War', 'Local Co-Op', 'Logic', 'Turn-Based Strategy', 'Roguelike', 'Turn-Based Combat', 'Dark Fantasy', 'Drama', 'Hack and Slash', 'Romance', 'Post-apocalyptic', '3D Platformer', 'Choose Your Own Adventure', 'Base Building', 'Historical', 'Memes', 'Roguelite', 'Turn-Based Tactics', 'Dating Sim', 'JRPG', 'Stealth', 'Web Publishing', 'Interactive Fiction', 'Walking Simulator', 'Hidden Object', 'Surreal', 'Narration', 'Classic', 'Dungeon Crawler', 'Party-Based RPG', 'Emotional', 'Fast-Paced', 'Military', 'Score Attack', 'Short', 'Bullet Hell', 'Third-Person Shooter', 'Hentai', 'Movie', '1990\'s', 'Nature', 'Software', 'Immersive Sim', 'Animation & Modeling', 'Team-Based', 'RTS', 'Robots', 'Top-Down Shooter', 'Isometric', 'Cyberpunk', 'Text-Based', 'Beautiful', 'Dark Humor', '2.5D', 'Aliens', 'Conversation', 'Experimental', 'Cinematic', 'Driving', 'Economy', 'Card Game', 'Music', 'RPGMaker', 'Abstract', 'LGBTQ+', 'Fighting', 'Investigation', '4 Player Local', 'Action Roguelike', 'Tutorial', 'Inventory Management', 'Nonlinear', 'Board Game', 'Tabletop', 'Perma Death', 'Flight', 'Audio Production', 'Soundtrack', 'Thriller', 'Real Time Tactics', 'Detective', 'Artificial Intelligence', 'Psychological', 'Arena Shooter', 'Strategy RPG', 'Moddable', 'Demons', 'Video Production', 'Tower Defense', 'NSFW', 'Modern', 'Clicker', 'Competitive', 'Lore-Rich', 'Life Sim', 'City Builder', 'Psychedelic', 'Destruction', 'Dystopian', 'Beat \'em up', 'Loot', 'Time Management', 'Precision Platformer', 'Metroidvania', 'Supernatural', 'Tactical RPG', 'Alternate History', 'Level Editor', 'Wargame', 'Comic Book', 'MMORPG', 'Game Development', 'Crime', 'Souls-like', 'Parkour', 'Dark Comedy', 'Character Action Game', 'World War II', 'Mythology', '2D Fighter', 'Runner', 'Grid-Based Movement', 'Philosophical', 'CRPG', 'Science', 'Twin Stick Shooter', 'Addictive', 'Automobile Sim', 'Co-op Campaign', 'Software Training', 'Class-Based', 'Grand Strategy', 'Space Sim', 'Blood', 'Gun Customization', 'Rhythm', 'Swordplay', 'Collectathon', 'Lovecraftian', 'Split Screen', 'Idler', 'Battle Royale', 'Cats', 'Dragons', 'Illuminati', 'Open World Survival Craft', 'Deckbuilding', 'Match 3', 'eSports', '3D Vision', '6DOF', 'America', 'Parody', 'Vehicular Combat', 'Noir', 'Card Battler', 'Conspiracy', 'Satire', 'Capitalism', '3D Fighter', 'Voxel', 'Trading', 'Bullet Time', 'Real-Time', 'Mouse only', 'Episodic', 'Political', 'Steampunk', 'Cult Classic', 'Epic', 'Photo Editing', 'Time Manipulation', 'Colony Sim', 'Mechs', 'Automation', 'Mystery Dungeon', 'Hunting', 'Time Travel', 'Gothic', 'Mining', 'Underground', 'Tanks', 'Agriculture', 'Dynamic Narration', 'Remake', 'MOBA', 'Otome', 'Farming Sim', 'Politics', 'Hacking', 'Ninja', 'Martial Arts', 'Quick-Time Events', 'Pirates', 'Word Game', 'God Game', 'Hero Shooter', 'Dog', 'Hex Grid', 'Spectacle fighter', 'Cold War', 'FMV', '4X', 'Solitaire', 'Combat Racing', 'Asynchronous Multiplayer', 'Looter Shooter', 'Trading Card Game', 'Superhero', 'Fishing', 'Creature Collector', 'Real-Time with Pause', 'Dinosaurs', 'Programming', 'Assassin', 'Underwater', 'Vampire', 'Trains', 'Naval', 'Kickstarter', 'Western', 'Heist', 'Immersive', 'Minigames', 'Narrative', 'Faith', 'Sokoban', 'Political Sim', 'GameMaker', 'Party', 'Archery', 'Cooking', 'Touch-Friendly', 'Experience', 'Diplomacy', 'Party Game', 'Mod', 'Foreign', 'Transportation', 'Snow', 'Sequel', 'Naval Combat', 'Auto Battler', 'Dungeons & Dragons', 'Documentary', 'Sailing', 'Music-Based Procedural Generation', 'Time Attack', 'Sniper', 'Games Workshop', 'Transhumanism', 'Soccer', 'Mars', 'Villain Protagonist', 'Gambling', 'World War I', 'Typing', 'Football', 'On-Rails Shooter', 'Offroad', 'Action RTS', 'Horses', 'Gaming', 'Werewolves', 'Silent Protagonist', 'Trivia', 'Crowdfunded', '360 Video', 'Chess', 'Nostalgia', 'Boxing', 'Farming', 'Traditional Roguelike', 'Unforgiving', 'LEGO', 'Roguelike Deckbuilder', 'TrackIR', 'Jet', 'Pinball', 'Outbreak Sim', 'Electronic Music', 'Spaceships', 'Rome', 'Golf', 'Motorbike', 'Ambient', 'Medical Sim', 'Asymmetric VR', 'Warhammer 40K', 'Based On A Novel', 'Spelling', 'Submarine', 'Bikes', 'Basketball', 'Roguevania', 'Escape Room', 'Social Deduction', 'Mini Golf', 'Intentionally Awkward Controls', 'Instrumental Music', 'Wrestling', 'Pool', 'Skateboarding', 'Vikings', 'Lemmings', 'Benchmark', 'Steam Machine', 'Baseball', 'Tennis', 'Hardware', 'Hockey', 'Skating', 'Electronic', 'Cycling', 'Motocross', 'Bowling', 'Rock Music', 'Feature Film', 'Voice Control', 'ATV', '8-bit Music', 'Well-Written', 'BMX', 'Skiing', 'Snowboarding', 'Boss Rush', 'Reboot']


function autocomplete(inp, arr) {
    /*the autocomplete function takes two arguments,
    the text field element and an array of possible autocompleted values:*/
    var currentFocus;
    /*execute a function when someone writes in the text field:*/
    inp.addEventListener("input", function (e) {
        var a, b, i, val = this.value;
        /*close any already open lists of autocompleted values*/
        closeAllLists();
        if (!val) { return false; }
        currentFocus = -1;
        /*create a DIV element that will contain the items (values):*/
        a = document.createElement("DIV");
        a.setAttribute("id", this.id + "autocomplete-list");
        a.setAttribute("class", "autocomplete-items");
        /*append the DIV element as a child of the autocomplete container:*/
        this.parentNode.appendChild(a);
        /*for each item in the array...*/
        for (i = 0; i < arr.length; i++) {
            /*check if the item starts with the same letters as the text field value:*/
            if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
                /*create a DIV element for each matching element:*/
                b = document.createElement("DIV");
                /*make the matching letters bold:*/
                b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
                b.innerHTML += arr[i].substr(val.length);
                /*insert a input field that will hold the current array item's value:*/
                b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
                /*execute a function when someone clicks on the item value (DIV element):*/
                b.addEventListener("click", function (e) {
                    /*insert the value for the autocomplete text field:*/
                    inp.value = this.getElementsByTagName("input")[0].value;
                    /*close the list of autocompleted values,
                    (or any other open lists of autocompleted values:*/
                    closeAllLists();
                });
                a.appendChild(b);
            }
        }
    });
    /*execute a function presses a key on the keyboard:*/
    inp.addEventListener("keydown", function (e) {
        var x = document.getElementById(this.id + "autocomplete-list");
        if (x) x = x.getElementsByTagName("div");
        if (e.keyCode == 40) {
            /*If the arrow DOWN key is pressed,
            increase the currentFocus variable:*/
            currentFocus++;
            /*and and make the current item more visible:*/
            addActive(x);
        } else if (e.keyCode == 38) { //up
            /*If the arrow UP key is pressed,
            decrease the currentFocus variable:*/
            currentFocus--;
            /*and and make the current item more visible:*/
            addActive(x);
        } else if (e.keyCode == 13) {
            /*If the ENTER key is pressed, prevent the form from being submitted,*/
            e.preventDefault();
            if (currentFocus > -1) {
                /*and simulate a click on the "active" item:*/
                if (x) x[currentFocus].click();
            }
        }
    });
    function addActive(x) {
        /*a function to classify an item as "active":*/
        if (!x) return false;
        /*start by removing the "active" class on all items:*/
        removeActive(x);
        if (currentFocus >= x.length) currentFocus = 0;
        if (currentFocus < 0) currentFocus = (x.length - 1);
        /*add class "autocomplete-active":*/
        x[currentFocus].classList.add("autocomplete-active");
    }
    function removeActive(x) {
        /*a function to remove the "active" class from all autocomplete items:*/
        for (var i = 0; i < x.length; i++) {
            x[i].classList.remove("autocomplete-active");
        }
    }
    function closeAllLists(elmnt) {
        /*close all autocomplete lists in the document,
        except the one passed as an argument:*/
        var x = document.getElementsByClassName("autocomplete-items");
        for (var i = 0; i < x.length; i++) {
            if (elmnt != x[i] && elmnt != inp) {
                x[i].parentNode.removeChild(x[i]);
            }
        }
    }
    /*execute a function when someone clicks in the document:*/
    document.addEventListener("click", function (e) {
        closeAllLists(e.target);
    });
} 