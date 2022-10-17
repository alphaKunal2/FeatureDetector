jQuery(function($) {
    var path = window.location.href; 
    // because the 'href' property of the DOM element is the absolute path
    $('ul a').each(function() {
      if (this.href === path) {
        $(this).addClass('active');
      }
    });
  });

  $(function($) {
    let url = window.location.href;
    $('ul li a').each(function() {
      if (this.href === url) {
        $(this).closest('li').addClass('selected');
      }
    });
  });


function fileinput() {
    $("#inputfile").trigger("click");
}



function onFileSelected(event) {
    var selectedFile = event.target.files[0];
    console.log($("#inputfile")[0].files);
    var reader = new FileReader();

    var imgtag = document.getElementById("inputImageDisplay");
    imgtag.title = selectedFile.name;

    reader.onload = function (event) {
        imgtag.src = event.target.result;
        var image_data = (imgtag.src.split(',')[1]);
        console.log(image_data);

        // console.log(imgtag.src);
        // var x = document.getElementById("inputfile").value;
        //   console.log(x);
        
    };

    reader.readAsDataURL(selectedFile);
}
















////////////////////////////////

$("#downloadInputImage").click(() => {
    var a = document.createElement('a');


    alert("Hello");
    var img = document.getElementById("inputImageDisplay");

    // atob to base64_decode the data-URI
    var image_data = atob(img.src.split(',')[1]);
    // console.log(image_data);
    // Use typed arrays to convert the binary data to a Blob
    var arraybuffer = new ArrayBuffer(image_data.length);
    var view = new Uint8Array(arraybuffer);
    for (var i=0; i<image_data.length; i++) {
        view[i] = image_data.charCodeAt(i) & 0xff;
       
    }
    try {
        // This is the recommended method:
        var blob = new Blob([arraybuffer], {type: 'image/jpeg'});
    } catch (e) {
        // The BlobBuilder API has been deprecated in favour of Blob, but older
        // browsers don't know about the Blob constructor
        // IE10 also supports BlobBuilder, but since the `Blob` constructor
        //  also works, there's no need to add `MSBlobBuilder`.
        var bb = new (window.WebKitBlobBuilder || window.MozBlobBuilder);
        bb.append(arraybuffer);
        var blob = bb.getBlob('image/jpeg'); // <-- Here's the Blob
    }

    // Use the URL object to create a temporary URL
    var url = (window.webkitURL || window.URL).createObjectURL(blob);

    a.href = url;
a.download = "input";
document.body.appendChild(a);
a.click();
document.body.removeChild(a);
    // location.href = url; // <-- Download!

});


$("#downloadOutputImage").click(() => {
    var a = document.createElement('a');


    
    var img = document.getElementById("inputImageDisplay");

    // atob to base64_decode the data-URI
    var image_data = atob(img.src.split(',')[1]);
    console.log(image_data);
    // Use typed arrays to convert the binary data to a Blob
    var arraybuffer = new ArrayBuffer(image_data.length);
    var view = new Uint8Array(arraybuffer);
    for (var i=0; i<image_data.length; i++) {
        view[i] = image_data.charCodeAt(i) & 0xff;
       
    }
    try {
        // This is the recommended method:
        var blob = new Blob([arraybuffer], {type: 'image/jpeg'});
    } catch (e) {
        // The BlobBuilder API has been deprecated in favour of Blob, but older
        // browsers don't know about the Blob constructor
        // IE10 also supports BlobBuilder, but since the `Blob` constructor
        //  also works, there's no need to add `MSBlobBuilder`.
        var bb = new (window.WebKitBlobBuilder || window.MozBlobBuilder);
        bb.append(arraybuffer);
        var blob = bb.getBlob('image/jpeg'); // <-- Here's the Blob
    }

    // Use the URL object to create a temporary URL
    var url = (window.webkitURL || window.URL).createObjectURL(blob);

    a.href = url;
a.download = "input.png";
document.body.appendChild(a);
a.click();
document.body.removeChild(a);
    // location.href = url; // <-- Download!

});
