class FileUpload {

    constructor(input) {
        this.input = input
        this.max_length = 1024 * 1024 * 10;
    }

    create_progress_bar() {
        var progress = `<div class="file-icon">
                            <i class="fa fa-file-o" aria-hidden="true"></i>
                        </div>
                        <div class="file-details">
                            <p class="filename"></p>
                            <small class="textbox"></small>
                            <div class="progress" style="margin-top: 5px;">
                                <div class="progress-bar bg-success" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%">
                                </div>
                            </div>
                        </div>`
        document.getElementById('uploaded_files').innerHTML = progress
    }

    upload() {
        this.create_progress_bar();
        this.initFileUpload();
    }

    initFileUpload() {
        this.file = this.input.files[0];
        this.upload_file(0, null);
    }

    //upload file
    upload_file(start, model_id) {
        var end;
        var self = this;
        var existingPath = model_id;
        var formData = new FormData();
        var nextChunk = start + this.max_length + 1;
        var currentChunk = this.file.slice(start, nextChunk);
        var uploadedChunk = start + currentChunk.size
        if (uploadedChunk >= this.file.size) {
            end = 1;
        } else {
            end = 0;
        }
        formData.append('file', currentChunk)
        formData.append('filename', this.file.name)
        $('.filename').text(this.file.name)
        $('.textbox').text("Uploading file")
        formData.append('end', end)
        formData.append('existingPath', existingPath);
        formData.append('nextSlice', nextChunk);
        $.ajaxSetup({
            headers: {
                "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
            }
        });
        $.ajax({
            xhr: function () {
                var xhr = new XMLHttpRequest();
                xhr.upload.addEventListener('progress', function (e) {
                    if (e.lengthComputable) {
                        if (self.file.size < self.max_length) {
                            var percent = Math.round((e.loaded / e.total) * 100);
                        } else {
                            var percent = Math.round((uploadedChunk / self.file.size) * 100);
                        }
                        $('.progress-bar').css('width', percent + '%')
                        $('.progress-bar').text(percent + '%')
                    }
                });
                return xhr;
            },

            url: '/fileUploader/',
            type: 'POST',
            dataType: 'json',
            cache: false,
            processData: false,
            contentType: false,
            data: formData,
            error: function (xhr) {
                alert(xhr.statusText);
            },
            success: function (res) {
                if (nextChunk < self.file.size) {
                    // upload file in chunks
                    existingPath = res.existingPath
                    self.upload_file(nextChunk, existingPath);
                } else {
                    // upload complete
                    $('.textbox').text(res.data);
                    alert(res.data)
                }
            }
        });
    };
}

(function ($) {
    $('#submit').on('click', (event) => {
        event.preventDefault();
        var uploader = new FileUpload(document.querySelector('#fileupload'))
        console.log(document.querySelector('#fileupload'));
        uploader.upload();
    });
})(jQuery);

ondragenter = function(evt) {
    evt.preventDefault();
    evt.stopPropagation();
};

ondragover = function(evt) {
    evt.preventDefault();
    evt.stopPropagation();
};

ondragleave = function(evt) {
    evt.preventDefault();
    evt.stopPropagation();
};

ondrop = function(evt) {
    evt.preventDefault();
    evt.stopPropagation();
    const files = evt.originalEvent.dataTransfer;
    var uploader = new FileUpload(files);
    uploader.upload();
};

$('#dropBox')
    .on('dragover', ondragover)
    .on('dragenter', ondragenter)
    .on('dragleave', ondragleave)
    .on('drop', ondrop);



    const $tabsToDropdown = $(".tabs-to-dropdown");

  function generateDropdownMarkup(container) {
    const $navWrapper = container.find(".nav-wrapper");
    const $navPills = container.find(".nav-pills");
    const firstTextLink = $navPills.find("li:first-child a").text();
    const $items = $navPills.find("li");
    const markup = `
      <div class="dropdown d-md-none">
        <button class="btn dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
          ${firstTextLink}
        </button>
        <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
          ${generateDropdownLinksMarkup($items)}
        </div>
      </div>
    `;
    $navWrapper.prepend(markup);
  }

  function generateDropdownLinksMarkup(items) {
    let markup = "";
    items.each(function () {
      const textLink = $(this).find("a").text();
      markup += `<a class="dropdown-item" href="#">${textLink}</a>`;
    });

    return markup;
  }

  function showDropdownHandler(e) {
    // works also
    //const $this = $(this);
    const $this = $(e.target);
    const $dropdownToggle = $this.find(".dropdown-toggle");
    const dropdownToggleText = $dropdownToggle.text().trim();
    const $dropdownMenuLinks = $this.find(".dropdown-menu a");
    const dNoneClass = "d-none";
    $dropdownMenuLinks.each(function () {
      const $this = $(this);
      if ($this.text() == dropdownToggleText) {
        $this.addClass(dNoneClass);
      } else {
        $this.removeClass(dNoneClass);
      }
    });
  }

  function clickHandler(e) {
    e.preventDefault();
    const $this = $(this);
    const index = $this.index();
    const text = $this.text();
    $this.closest(".dropdown").find(".dropdown-toggle").text(`${text}`);
    $this
      .closest($tabsToDropdown)
      .find(`.nav-pills li:eq(${index}) a`)
      .tab("show");
  }

  function shownTabsHandler(e) {
    // works also
    //const $this = $(this);
    const $this = $(e.target);
    const index = $this.parent().index();
    const $parent = $this.closest($tabsToDropdown);
    const $targetDropdownLink = $parent.find(".dropdown-menu a").eq(index);
    const targetDropdownLinkText = $targetDropdownLink.text();
    $parent.find(".dropdown-toggle").text(targetDropdownLinkText);
  }

  $tabsToDropdown.each(function () {
    const $this = $(this);
    const $pills = $this.find('a[data-toggle="pill"]');

    generateDropdownMarkup($this);

    const $dropdown = $this.find(".dropdown");
    const $dropdownLinks = $this.find(".dropdown-menu a");

    $dropdown.on("show.bs.dropdown", showDropdownHandler);
    $dropdownLinks.on("click", clickHandler);
    $pills.on("shown.bs.tab", shownTabsHandler);
  });
