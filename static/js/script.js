document.addEventListener("DOMContentLoaded", function() {
    const downloadButton = document.getElementById("download-button");
    downloadButton.addEventListener("click", downloadSong);

    function downloadSong() {
        const urlInput = document.getElementById("url");
        const url = urlInput.value;

        const xhr = new XMLHttpRequest();
        xhr.open("POST", "/download", true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function() {
            if (xhr.readyState === XMLHttpRequest.DONE) {
                if (xhr.status === 200) {
                    showStatusMessage(xhr.responseText);
                } else {
                    showStatusMessage("Error en la descarga");
                }
            }
        };
        xhr.send(JSON.stringify({ url: url }));
    }

    function showStatusMessage(message) {
        const statusMessage = document.getElementById("status");
        statusMessage.textContent = message;
    }
});
