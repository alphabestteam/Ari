const img = document.getElementById("loader");
const menu = document.getElementById("menu");
const orderSummary = document.getElementById("order-summary")
const latestOrders = document.getElementById("latest-order-info")

async function fetchData() {
  await fetch("http://localhost:8000/menu").then(async (response) => {
    img.style.display = "none";

    try {
      const data = await response.json();

      for (const key in data) {
        let object = data[key];
        for (const property in object) {
          const item = object[property];

          const menuItem = document.createElement("div");
          menuItem.className = "item";
          menu.appendChild(menuItem);

          const description = document.createElement("p");
          description.textContent = item["description"];
          menuItem.appendChild(description);

          const title = document.createElement("h3");
          price = item["price"].toFixed(2)
          title.textContent = item["name"] + " ($" + price  + ")" ;
          menuItem.appendChild(title);
          const quantity = document.createElement("input");
          quantity.value = 0;
          quantity.id = "id-item";
          quantity.setAttribute("type", "number");
          quantity.setAttribute("min", "0");
          quantity.setAttribute("max", "5");
          menuItem.appendChild(quantity);
        }
      }

    } catch (error) {
      console.error("Error:", error);
    }

      const addItem = document.getElementById("id-item")
      addItem.addEventListener("click", () => {
      const menuItemOrder = document.createElement("p");
      menuItemOrder.textContent = (addItem.value)
      orderSummary.appendChild(menuItemOrder)
    });
  });
}

fetchData();

/*
List of endpoints:
  GET - http://localhost:8000/hello -> {'Hello': 'World'} Here as an example
  GET - http://localhost:8000/menu -> {'items': menu} A dict of the menu
  POST - http://localhost:8000/latest-order -> A dict of the latest order
  POST - http://localhost:8000/orders -> An endpoint to handle an order. The order is in the http body as so: { 'items': items }

*/
