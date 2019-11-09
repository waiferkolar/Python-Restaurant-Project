function getAllTable() {
    eel.getAllTable()((data) => {
        let str = "";
        console.info(data)
        data.forEach((table) => {
            console.info(table)
            str += `
           <tr class="text-white">
                    <td>${table[0]}</td>
                    <td>${table[1]}</td>
                    <td>Engage</td>
                    <td><button class="btn btn-info btn-sm">Bill Out</button></td>
                    <td>
                        <button class="btn btn-outline-warning btn-sm">Edit</button>
                        <button class="btn btn-outline-danger btn-sm">Delete</button>
                    </td>
                </tr>
           `;
        });
        document.getElementById("table-holder").innerHTML = str;
    })
}