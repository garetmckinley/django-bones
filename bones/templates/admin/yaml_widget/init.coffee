$ ->
  row = $(".field-yaml_actions")
  content = $("#id_yaml_actions").val()
  row.html("loading widget...")
  $.get '/static/bones/admin/yaml_widget/view.html', (data) ->
    row.html(data)
    editor = ace.edit("yaml-editor")
    editor.setTheme("ace/theme/tomorrow")

    editor.getSession().setMode("ace/mode/yaml")
    raw = $("#id_yaml_actions")
    editor.setValue(content, 1)
    raw.val(content)
    editor.getSession().on "change", ->
      raw.val(editor.getSession().getValue())
      return


