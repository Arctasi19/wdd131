import recipes from "./recipes.mjs";

function recipeTemplate(recipe) {
	return `<figure class="recipe-card">
	<img src="${recipe.image}" alt="image of ${recipe.name} on a plate" />
	<figcaption>
		<ul class="tags-container">
			${tagsTemplate(recipe.tags)}
		</ul>
		<h2><a href="#">${recipe.name}</a></h2>
		<p class="rating">
			<span
				class="rating"
				role="img"
				aria-label="Rating: ${recipe.rating} out of 5 stars"
			>
				${ratingTemplate(recipe.rating)}
			</span>
		</p>
		<p class="description">
			${recipe.description}
		</p>
</figcaption>
</figure>`;
}

function randNumGen(number) {
    return Math.floor(Math.random()*number);
}

function getRandomListItem(list) {
    const listLength = list.length;
    const randIndex = randNumGen(listLength);
    return list[randIndex];
}

function tagsTemplate(tags) {
    let html = '';
    for (let tag of tags) {
        html += `<li class="tag">${tag}</li>`;
    }

	return html;
}

function ratingTemplate(rating) {
	let html = `<span
	class="rating"
	role="img"
	aria-label="Rating: ${rating} out of 5 stars"
>`
    for (let i = 1; i <= 5; i++) {
        if (i <= rating) {
            html += `<span aria-hidden="true" class="icon-star">⭐</span>`
        }
        else {
            html += `<span aria-hidden="true" class="icon-star-empty">☆</span>`
        }
    }
	html += `</span>`
	return html
}

function renderRecipes(recipeList) {
    const outputElement = document.querySelector(".recipes-container");
    outputElement.innerHTML = ""; 

    let html = '';
    for (let recipe of recipeList) {
        html += recipeTemplate(recipe);
    }

    outputElement.innerHTML = html;
}

function filterFunction(recipe) {
    const query = this.query; 

    const textMatch = recipe.name.toLowerCase().includes(query) || recipe.description.toLowerCase().includes(query);

    const tagMatch = recipe.tags.find((tag) => tag.toLowerCase().includes(query));

    const ingredientMatch = recipe.recipeIngredient.find((ingredient) => ingredient.toLowerCase().includes(query));

    return textMatch || tagMatch || ingredientMatch;
}

function sortFunction(recipeA, recipeB) {
    const nameA = recipeA.name.toUpperCase();
    const nameB = recipeB.name.toUpperCase();

    if (nameA < nameB) {
        return -1;
    }
    if (nameA > nameB) {
        return 1;
    }
    return 0;
}

function filter(query) {
	const filtered = recipes.filter(filterFunction, { query: query }) 
	
	const sorted = filtered.sort(sortFunction)
	return sorted
}

function searchHandler(event) {
	event.preventDefault()
	
    const input = document.querySelector("#search").value;
  
    const query = input.toLowerCase();
  
    const filteredRecipes = filter(query);
  
    renderRecipes(filteredRecipes);
}

function init() {
  const recipe = getRandomListItem(recipes)
  renderRecipes([recipe]);
}

init();

document.querySelector("#search-button").addEventListener("click", searchHandler);