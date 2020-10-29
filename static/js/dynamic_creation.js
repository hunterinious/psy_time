$(function () {

    var customSelect = $('.customselect')
    customSelect.select2()

    var id = undefined
    var form_name = ''
    var select2 = $('.select2-selection')
    var target = undefined


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

                target.children('span')[0].nextSibling.textContent = data[data.length -1].name

                data.forEach(e => {
                   if(select_val.includes(e.id)){
                        select.append(`<option selected value=${e.name} data-url=${e.data_url} delete-url=${e.delete_url}>${e.name}</option>`)
                    }
                   else{
                        select.append(`<option value=${e.name} data-url=${e.data_url} delete-url=${e.delete_url}>${e.name}</option>`)
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


    $("#modal-dynamic").on("submit", e=> saveForm())

    $(".dynamic-create").click(e => {
        id = e.target.id
        url = e.target.getAttribute("data-url")
        form_name = 'create-form'
        loadForm(e, url)
    })


    select2.dblclick(e => {
        if(e.target.tagName === 'LI'){
            var closestElem = $(e.currentTarget).closest("div[id*='-div']")
            id = closestElem.attr('id').split('-')[0]
            target = $(event.target)
            var name = target.text().replace('×', '')
            var option = closestElem.find(`select option:contains(${name})`)
            url = option.attr('data-url')
//            url = e.target.getAttribute("data-url")
            form_name = 'update-form'
            loadForm(e, url)
        }
    })

//    customSelect.keydown(e => {
//        var currentTarget = $(e.currentTarget)
//        var target = currentTarget.find(`option[value=${option_id}]`)
//        if(e.keyCode == 8) {
//            if (target.val()){
//                id = currentTarget.closest("div[id*='-div']").attr('id').split('-')[0]
//                url = target.attr("delete-url")
//                form_name = 'delete-form'
//                loadForm(e, url)
//            }else{
//                alert("You need to reselect option, which you want to delete")
//            }
//        }
//    })

})