let discounts = new Map([
    [50000, 0.85],
    [10000, 0.9],
    [7000, 0.93],
    [5000, 0.95],
    [1000, 0.97]
]);

var discount_factor = 1

function update(){
    var input = ['count', 'price', 'state_code'],
        form = document.getElementById('main_form'),
        spinner = document.getElementById('spinner');
    input.forEach(function(name, index){
        input[index] = Number(document.getElementById(name).value);
    });
    
    show_discount(input[0]);

    if (!form.checkValidity()){
        result = "";
    }
    else {
        spinner.removeAttribute('hidden');
        result = calculate(input[0], input[1], input[2], discount_factor);
        setTimeout(function(){ spinner.setAttribute('hidden','');}, 500);
    }
    document.getElementById('result').value = result;
}

function show_discount(count){
    for (item of document.getElementsByClassName('list-group-item')){ item.classList.remove('list-group-item-primary');}
    for (let [key, value] of discounts.entries()){
        if (count >= key){
            discount_factor = value;
            document.getElementById('discount_'+key.toString()).classList.add('list-group-item-primary');
            break;
        }
    }

}

function calculate(count, price, taxes, discount_factor){
    result = 0;
    result = count * price * discount_factor;
    result += result * taxes;
    return result;
}