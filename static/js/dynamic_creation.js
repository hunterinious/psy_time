$(function () {

    var customSelect = $('.customselect')
    customSelect.select2()

    var id = undefined
    var form_name = ''
    var modalChoice = $('#modal-choice')
    var select2 = $('.select2-selection__rendered')
    var target = undefined

    var load = function (e, url) {
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
    }

    var loadChoice = function (e, url) {
        load(e, url)
    }

    var loadForm = function (e, url) {
        load(e, url)
    };

    var saveForm = () => {
        var form = $(`.${id}-${form_name}`);
        $.ajax({
          url: form.attr("action"),
          data: form.serialize(),
          type: form.attr("method"),
          dataType: 'json',
          success: function (data) {
            if (data.form_is_valid) {
                var data = data['data']

                var select = $(`#${id}-div select`)
                var select_val = select.val()

                select.empty()

                if(form_name == 'update-form'){
                    target.children('span')[0].nextSibling.textContent = data.name
                }

                if(form_name == 'delete-form'){
                    target.remove()
                }

                data.forEach(e => {
                   if(select_val.includes(e.id.toString())){

                        select.append(`<option selected value=${e.id} data-url=${e.data_url} delete-url=${e.delete_url}>${e.name}</option>`)
                    }
                   else{
                        select.append(`<option value=${e.id} data-url=${e.data_url} delete-url=${e.delete_url}>${e.name}</option>`)
                   }
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


    select2.dblclick(e => {
        var option = undefined
        if(e.target.tagName === 'LI'){
            var closestElem = $(e.currentTarget).closest("div[id*='-div']")
            id = closestElem.attr('id').split('-')[0]
            target = $(e.target)
            var name = target.text().replace('×', '')
            option = closestElem.find(`select option:contains(${name})`)
            var url = modalChoice.attr('get-url')
            loadChoice(e, url)

            $(document).unbind('click')

            $(document).on('click', '#update-selected', function(e) {
                form_name = 'update-form'
                loadForm(e, option.attr('data-url'))
            });

            $(document).on('click', '#delete-selected', function(e) {
                form_name = 'delete-form'
                loadForm(e, option.attr('delete-url'))
            });
        }
    })
})