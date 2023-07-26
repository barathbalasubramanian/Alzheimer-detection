

document.addEventListener('DOMContentLoaded', function() {

    const fileInput = document.querySelector("input[type=file]");
        fileInput.addEventListener("change", function(e) {
        const uploadFileParent = this.closest(".uploadFile");
        const filenameElement = uploadFileParent.querySelector(".filename");
        filenameElement.textContent = e.target.files[0].name;
        console.log('Done')
    });
});