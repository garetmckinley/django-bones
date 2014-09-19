$ ->
  row = $(".field-coffee_input")
  content = $("#id_coffee_input").val()
  row.html("loading widget...")
  $.get '/static/bones/admin/coffee_widget/view.html', (data) ->
    row.html(data)
    editor = ace.edit("coffee_input-editor")
    editor.setTheme("ace/theme/tomorrow")

    editor.getSession().setMode("ace/mode/coffee")
    raw = $("#id_coffee_input")
    editor.setValue(content, 1)
    raw.val(content)
    editor.getSession().on "change", ->
      raw.val(editor.getSession().getValue())
      return


