$(function () {
    let id = undefined
    let option_id = undefined
    let form_name = ''

    var loadForm = function (e) {
        let data_url = e.target.getAttribute("data-url")

        $.ajax({
          url: data_url,
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
        let method = form.attr("method")

        $.ajax({
          url: form.attr("action"),
          data: form.serialize(),
          type: method,
          dataType: 'json',
          success: function (data) {
            if (data.form_is_valid) {
              let select = $(`#${id}-div select`)
              if (data.method === 'create') {
                let data_url = select.children().first().attr('data-url')
                let length = select.children().length + 1
                data_url = data_url.replace(/\d+/, length)
                select.append(`<option value=${length} data-url=${data_url}>${data.name}</option>`)
              } else if(data.method === 'update'){
                select.find(`option[value=${option_id}]`).text(data.name)
              }
              $("#modal-dynamic").modal("hide");
            }
            else {
              $("#modal-dynamic .modal-content").html(data.html_form);
            }
          }
        });
        return false;
     };

     $(".dynamic-create").click(e => {
        id = e.target.id
        form_name = 'create-form'
        loadForm(e)
     })
     $("#modal-dynamic").on("submit", e => saveForm())

     $('.customselect').dblclick(e => {
        target = e.target
        if(target.tagName === 'OPTION'){
            option_id = target.value
            id = $('.customselect').parents("div[id*='-div']").attr('id').split('-')[0]
            form_name = 'update-form'
            loadForm(e)
        }
    })
})