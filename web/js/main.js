let divAry = ["Home-Page", "Table-Page", "Dish-Page", "Order-Page", "User-Page"];

function toggleDiv(page) {
    divAry.forEach((currnetPage) => {
        document.getElementById(currnetPage).style.display = "none";
    });
    switch (page) {
        case "Table-Page":
            getAllTable(); break;
    }
    document.getElementById(page).style.display = "block";
}

toggleDiv('Home-Page');