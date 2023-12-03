document.addEventListener('DOMContentLoaded', function () {
    const newsContainer = document.getElementById('newsContainer');

    // ... (existing styles)

    // Add styles to the search form
    const searchForm = document.createElement('form');
    searchForm.id = 'searchForm';

    const searchInput = document.createElement('input');
    searchInput.type = 'text';
    searchInput.id = 'searchInput';
    searchInput.placeholder = 'Search Articles';

    const searchButton = document.createElement('button');
    searchButton.type = 'button';
    searchButton.textContent = 'Search';
    searchButton.addEventListener('click', function () {
        const searchTerm = document.getElementById('searchInput').value;
        searchNews(searchTerm);
    });

    searchForm.appendChild(searchInput);
    searchForm.appendChild(searchButton);

    // Insert the search form before the news container
    newsContainer.parentNode.insertBefore(searchForm, newsContainer);

    // ... (existing styles)

    function searchNews(searchTerm) {
        // Perform search and update the news container accordingly
        // You can use the same fetch method used in getNews function
        // and update the newsContainer.innerHTML with the search results.
    }
});
