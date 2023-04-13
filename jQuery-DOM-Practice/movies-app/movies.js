let currentId = 0;

//list of all movies to add to or remove from
let movieList = [];

$(function(){
    $("#new-movie-form").on("submit", function(sumbitE) {
        sumbitE.preventDefault();
        let title = $("#title").val();
        let rating = $("#rating").val();

        let movieData = { title, rating, currentId};
        const HTMLtoAppend = createMovieDataHTML(movieData);

        currentId++
        movieList.push(movieData);

        $("#movie-table-body").append(HTMLtoAppend);
        $("#new-movie-form").trigger("reset");
    })
  
    $("tbody").on("click", ".btn.btn-delete", function(deleteE) {
      // find the index where this movie is
      let indexToRemoveAt = moviesList.findIndex(movie => movie.currentId === +$(deleteE.target).data("deleteId"))
      
      // remove it from the array of movies
      moviesList.splice(indexToRemoveAt, 1)
  
      // remove it from the DOM
      $(deleteE.target)
        .closest("tr")
        .remove();
    });
})


function createMovieDataHTML(data) {
    return `
      <tr>
        <td>${data.title}</td>
        <td>${data.rating}</td>
        <td>
          <button class="btn btn-delete" data-delete-id=${data.currentId}>
            Delete
          </button>
        </td>
      <tr>
    `;
  }

  //jQuery for styling
  $(".main-heading").

  $("body").css("background-color", "blue");