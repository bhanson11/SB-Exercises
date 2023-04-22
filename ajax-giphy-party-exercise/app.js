console.log("Let's get this party started!");

const $searchInput = $('#search');
const $gifGrid = $('#gif-grid');

function addGif(res) {
    let numResults = res.data.length;
    if (numResults) {
        let randomIdx = Math.floor(Math.random() * numResults);
        let $newCol = $("<div>", { class: "col-4 mb-3" });
        let $newGif = $("<img>", {
            src: res.data[randomIdx].images.original.url,
            class: "w-100"
        });
        $newCol.append($newGif);
        $gifGrid.append($newCol);
    }
}

$("form").on("submit", async function(e) {
    e.preventDefault();

    let searchTerm = $searchInput.val();
    $searchInput.val("");

    const response = await axios.get("https://api.giphy.com/v1/gifs/search", {
        params: {
            q: searchTerm,
            api_key: "3smNW7uMkvoAMdpIJkAhKfTmO4aUszjo"
        }
    });

    addGif(response.data);
});

$('#remove').on("click", function() {
    $gifGrid.empty();
});