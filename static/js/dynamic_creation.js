$(function () {
    let id = undefined
    let form_name = ''
    let customSelect = $('.customselect')

    var loadForm = function (e, url) {
        $.ajax({
          url: url,
          type: 'get',
          dataType: 'json',
          beforeSend: function () {
            $("#modal-dynamic").modal("show");
          },
          success: function (data) {
            $("#modal-dynamic .modal-content").html(data.html_form);
          }
        });
    };

    var saveForm = function() {
        let form = $(`.${id}-${form_name}`);
        $.ajax({
          url: form.attr("action"),
          data: form.serialize(),
          type: form.attr("method"),
          dataType: 'json',
          success: function (data) {
            if (data.form_is_valid) {
                let select = $(`#${id}-div select`)

                select.empty()

                data['data'].forEach(e => {
                   select.append(`<option value=${e.id} data-url=${e.data_url} delete-url=${e.delete_url}>${e.name}</option>`)
                })

                $("#modal-dynamic").modal("hide");
            }
            else {
                $("#modal-dynamic .modal-content").html(data.html_form);
            }
          }
        });
        return false;
     };


    $("#modal-dynamic").on("submit", e => saveForm())

    $(".dynamic-create").click(e => {
        id = e.target.id
        url = e.target.getAttribute("data-url")
        form_name = 'create-form'
        loadForm(e, url)
    })

    customSelect.dblclick(e => {
        if(e.target.tagName === 'OPTION'){
            id = $('.customselect').parents("div[id*='-div']").attr('id').split('-')[0]
            url = e.target.getAttribute("data-url")
            form_name = 'update-form'
            loadForm(e, url)
        }
    })

    $('.customselect').keyup(e => {
        let value = customSelect.val()
        value = value[value.length - 1]
        target = customSelect.find(`option[value=${value}]`)
        if(e.keyCode == 8) {
            if (customSelect.val()){
                id = customSelect.parents("div[id*='-div']").attr('id').split('-')[0]
                url = target.attr("delete-url")
                form_name = 'delete-form'
                loadForm(e, url)
            }
        }
    })

})