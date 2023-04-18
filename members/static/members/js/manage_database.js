const checkboxes = document.getElementsByName("row_checkbox");
const memberIdInput = document.getElementById("member_id");
const selectAllCheckbox = document.getElementById("select_all");
const selectedRowsInput = document.getElementById('selected_rows');
const selectedRowIds = [];

for (const checkbox of checkboxes) {
    checkbox.addEventListener("change", function() {
        if (checkbox.checked) {
            memberIdInput.value = checkbox.value;
        } else {
            memberIdInput.value = "";
        }
    });
}

selectAllCheckbox.addEventListener("change", function() {
    for (const checkbox of checkboxes) {
        checkbox.checked = selectAllCheckbox.checked;
    }
});

document.getElementById("update_rows_form").addEventListener("submit", function(event) {
    let selectedCount = 0;
    for (const checkbox of checkboxes) {
        if (checkbox.checked) {
            selectedCount++;
            memberIdInput.value = checkbox.value;
        }
    }

    if (selectedCount === 0) {
        event.preventDefault();
        alert("Please select a row to edit.");
    } else if (selectedCount > 1) {
        event.preventDefault();
        alert("Cannot edit multiple rows, please select one.");
    }
});

document.getElementById('delete-form').addEventListener('submit', function (event) {
    for (const checkbox of checkboxes) {
        if (checkbox.checked) {
            selectedRowIds.push(checkbox.value);
        }
    }

    selectedRowsInput.value = selectedRowIds.join(',');

    if (selectedRowIds.length === 0) {
        event.preventDefault();
        alert('Please select at least one row to delete.');
    }
});

window.addEventListener('load', function() {
    for (const checkbox of checkboxes) {
        checkbox.checked = false;
    }
});
