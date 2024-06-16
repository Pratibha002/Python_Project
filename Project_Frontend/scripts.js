document.getElementById('ok-button').addEventListener('click', function() {
    document.getElementById('options-box').style.display = 'block';
});

document.getElementById('next-button').addEventListener('click', function() {
    const action = document.getElementById('action-select').value;
    if (action === 'pdf') {
        document.getElementById('snapshot-box').style.display = 'block';
    } else {
        // Code to download video
        alert('Downloading video...');
    }
});

document.getElementById('generate-pdf').addEventListener('click', function() {
    const interval = document.getElementById('interval').value;
    // Code to generate PDF with snapshots
    alert(`Generating PDF with snapshots every ${interval} seconds...`);
});
