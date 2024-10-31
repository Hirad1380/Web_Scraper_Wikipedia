window.onload = () => {
    var readers = [],
        x = document.getElementById("field"),
        files = document.getElementById("file"),
        table = document.getElementById("table"),
        cont_table = document.getElementById("cont_tbl"),
        main = document.getElementById("main"),
        searchInput = document.getElementById("search-input");
    let rows = [];

    files.onchange = () => {
        
        table.innerHTML = "";
        rows = [];

        
        for (let i = 0; i < files.files.length; i++) {
            let reader = new FileReader();
            readers.push(reader);

            reader.onloadend = () => {
                let csv = reader.result;

                
                let fileRows = csv.trim().split('\n').map(row => row.split(','));
                rows = rows.concat(fileRows);

                
                if (readers.every(reader => reader.readyState === FileReader.DONE)) {
                    generateTable();
                }
            };

            reader.readAsText(files.files[i]);
        }

        x.style.display = "none";
        main.style.display = "block";
        cont_table.style.display = "block";
    };

    function generateTable() {
        let html = '<table><thead><tr>';
        rows[0].forEach(header => {
            html += `<th>${header}</th>`;
        });
        html += '</tr></thead><tbody>';
        rows.slice(1).forEach(row => {
            html += '<tr>';
            row.forEach(cell => {
                html += `<td>${cell}</td>`;
            });
            html += '</tr>';
        });
        html += '</tbody></table>';

        table.innerHTML = html;
    }

    function searchCSV(query) {
        let results = [];
        if (rows.length > 0) {
            rows.forEach((row, index) => {
                row.forEach(col => {
                    let value = col.trim(); 
                    if (value.toLowerCase().includes(query.toLowerCase())) {
                        results.push(index);
                    }
                });
            });
        }
        return results;
    }

    function displayResults(results) {
        if (results.length === 0) {
            // console.log("No results found for the search query.");
            alert("No results found for the search query.")
        }
    
        table.querySelectorAll('tr').forEach((row, index) => {
            if (results.includes(index)) {
                row.style.display = "";
            } else {
                row.style.display = "none";
            }
        });
    }

    searchInput.addEventListener('input', () => {
        const query = searchInput.value.trim();
        const results = searchCSV(query);
        displayResults(results);


        fetch('Word_count.csv')
        .then(response => response.text())
        .then(csv => {
            processData(csv);
        })
        .catch(error => console.error('Error fetching CSV file:', error));

        function processData(csv) {
            const rows = csv.trim().split('\n').map(row => row.split(','));
            const firstColumns = rows.map(row => [row[0]]);
            const SecondColumns = rows.map(row => [row[1]]);
            console.log(firstColumns);
            console.log(SecondColumns);
            for(i = 0; i < firstColumns.length; i++){
                if(query == firstColumns[i]){
                    console.log("Query: "+ query + " ------- Column: " + firstColumns[i] + " ----- i: " + i)
                    var Tableno = SecondColumns[i] - 1
                    alert("Table Number: " + Tableno)
                }
            }
        }
    
        const filter = searchInput.value.toUpperCase();
        const cells = document.querySelectorAll("#table td");
    
        if (filter === "") {
            cells.forEach(cell => {
                cell.innerHTML = cell.textContent;
            });
            return;
        }
        cells.forEach(cell => {
            let textValue = cell.textContent;
            if (textValue.toUpperCase().indexOf(filter) > -1) {
                textValue = textValue.replace(
                    new RegExp(filter, "gi"),
                    '<span class="highlight">$&</span>'
                );
                cell.innerHTML = textValue;
            } else {
                cell.innerHTML = textValue;
            }
        });
    });
};