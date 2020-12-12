// JavaScript source code
var total, bagQty;
var ingridents; // jasonify it 

var cart = [];



function addToCart(itemId, itemName, itemPrice) {
    let newItem = {
        "itemId": itemId,
        "itemName": itemName,
        "itemPrice": itemPrice
    }
    cart.push(newItem);

}
function removeFromCart(itemId) {
    console.log(cart.find(itemId));
}
function createFromList() {

}

window.loadHTML = loadHTML();