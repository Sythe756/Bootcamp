    //insertRow() should add another row to the table
    let i = 1
    let j = 1
    function insertRow(){
      let table = document.getElementById("sampleTable");
      let row = table.insertRow(table.rows.length);
      var cell1 = row.insertCell(0);
      var cell2 = row.insertCell(1);
      cell1.innerHTML = "Row "+ j++ +" cell " + i++;
      cell2.innerHTML = "Row "+ j++ +" cell " + i++;

    }