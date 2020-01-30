new Chart(document.getElementById("pie-chart"), {
    type: 'pie',
    data: {
        labels: ["Fruits", "Vegies", "Skin-Care", "Cold Drink", "Beverage"],
        datasets: [{
            label: "Population (millions)",
            backgroundColor: ["#3e95cd", "#8e5ea2", "#3cba9f", "#e8c3b9", "#c45850"],
            data: [2478, 5267, 734, 784, 433]
        }],
        fontColor: 'white'

    },
    options: {
        legend: {
            labels: {
                fontColor: 'black'
            }
        },
        title: {
            display: true,
            fontColor: 'black',
            text: 'Product Category Sales Monthly Chart'
        },


    }
});
