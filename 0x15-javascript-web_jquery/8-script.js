$(document).ready(function () {
  $.ajax({
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    method: 'GET',
    success: function (data) {
      const listMovies = $('#list_movies');
      $.each(data.results, function (index, movie) {
        listMovies.append('<li>' + movie.title + '</li>');
      });
    },
    error: function () {
      $('#list_movies').text('Failed to fetch film title');
    }
  });
});
