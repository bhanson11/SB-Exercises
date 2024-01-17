async function submitWord() {
    console.log('Submitting word...');
    try {
        const word = $("#wordInput").val();
        console.log("Word:", word);

        const response = await axios.post('/submit-word', { word: word });
        console.log("Response:", response.data);

        // Handle the JSON response from the server
        const result = response.data.result;
        const score = response.data.score; 
        const guessedWords = response.data.guessed_words;  // Explicitly access guessed_words field

        displayResultMessage(result);
        updateScore(score);
        displayGuessedWords(guessedWords);  // Pass guessedWords to the function

        // Clear the input field
        $("#wordInput").val("");

    } catch (error) {
        console.error(error);
    }


function displayResultMessage(result) {
    // Update the UI to display the result message
    const resultContainer = $(".message");
    if (result === 'ok') {
        resultContainer.text('The word is valid and exists on the board!');
    } else if (result === 'not-on-board') {
        resultContainer.text('The word is valid but does not exist on the board.');
    } else if (result === 'not-word') {
        resultContainer.text('The word is not valid.');
    }
}

function displayGuessedWords(guessedWords) {
    console.log('Guessed Words:', guessedWords);

    // Update UI to display list of guessed words
    const wordsContainer = $(".words");
    wordsContainer.empty();

    if (guessedWords) {
        guessedWords.forEach(word => {
            wordsContainer.append(`<li>${word}</li>`);
        });
    } else {
        console.error('Guessed words is not an array or is undefined:', guessedWords);
    }
}

function updateScore(score) {
    //Update UI to display current score
    const scoreContainer = $(".score");
    scoreContainer.text(score);
}

$(document).ready(function () {
    $(".submit-word").submit(submitWord); // Attach the submitWord function to the form submit event
});

document.addEventListener("DOMContentLoaded", function () {
    $("#submitButton").click(function (evt) {
        evt.preventDefault();
        submitWord();
    });
});
}
// function showTimer() {
//     $(".timer", this.board).text(this.secs);
// }

// async function tick() {
//     this.secs -= 1;
//     this.showTimer();

//     if (this.secs === 0) {
//         clearInterval(this.timer);
//         await this.scoreGame();
//     }
// }

// /* end of game: score and update message. */

// async function scoreGame() {
//     $(".add-word", this.board).hide();
//     const resp = await axios.post("/post-score", { score: this.score });
//     if (resp.data.brokeRecord) {
//       this.showMessage(`New record: ${this.score}`, "ok");
//     } else {
//       this.showMessage(`Final score: ${this.score}`, "ok");
//     }
//   }
// }


// async function submitWord(evt) {
//     evt.preventDefault();
//     const $word = $(".word", this.board);

//     let word = $word.val();
//     if (!word) return;

//     if (this.words.has(word)) {
//         this.showMessage('Already found ${word}', "err");
//         return;
//     }
    
//     // check server for validity
//     const resp = await axios.get("/submit-word", { params: { word: word }});
//     if (resp.data.result === "not-word") {
//       this.showMessage(`${word} is not a valid English word`, "err");
//     } else if (resp.data.result === "not-on-board") {
//       this.showMessage(`${word} is not a valid word on this board`, "err");
//     } else {
//       this.showWord(word);
//       this.score += word.length;
//       this.showScore();
//       this.words.add(word);
//       this.showMessage(`Added: ${word}`, "ok");
//     }

//     $word.val("").focus();
//   }