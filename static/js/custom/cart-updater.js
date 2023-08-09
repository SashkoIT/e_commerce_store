window.addEventListener("load", solve);

function solve() {
    const updateButton = document.getElementById('update-button');
    const fruitsQuantities = document.getElementsByClassName('quantity');
    const sum = document.getElementById('sum');
    const final = document.getElementById('final');
    const shipping = document.getElementById('shipping');
    updateButton.addEventListener('click', resultHandler);


    function resultHandler() {
        let result = 0;
        for (const fruitQuantity of fruitsQuantities) {
            let priceKG = document.getElementById('price')
            result += Number(fruitQuantity.value) * Number(priceKG.textContent)
        }
        sum.textContent = result;
        if (result >= 75) {
            final.textContent = result
            shipping.textContent = 'FREE';
        } else {
            final.textContent = result + 20;
            shipping.textContent = '$20';
        }
    }
}

