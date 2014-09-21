(($) ->
  pasteIntoInput = (el, text) ->
    el.focus()
    val = el.value
    if typeof el.selectionStart is "number"
      selStart = el.selectionStart
      el.value = val.slice(0, selStart) + text + val.slice(el.selectionEnd)
      el.selectionEnd = el.selectionStart = selStart + text.length
    else unless typeof document.selection is "undefined"
      textRange = document.selection.createRange()
      textRange.text = text
      textRange.collapse false
      textRange.select()
    return
  allowTabChar = (el) ->
    $(el).keydown (e) ->
      if e.which is 9
        pasteIntoInput this, "    "
        false


    # For Opera, which only allows suppression of keypress events, not keydown
    $(el).keypress (e) ->
      false  if e.which is 9

    return
  $.fn.allowTabChar = ->
    if @jquery
      @each ->
        if @nodeType is 1
          nodeName = @nodeName.toLowerCase()
          allowTabChar this  if nodeName is "textarea" or (nodeName is "input" and @type is "text")
        return

    this

  return
) jQuery
$ ->
  $("textarea").allowTabChar()
  return

$ ->
  row = $(".field-content")
  content = $("#id_content").val()
  row.html("loading widget...")
  $.get '/static/bones/admin/vue_widget/view.html', (data) ->
    row.html(data)
    new Vue(
      el: "#editor"
      data:
        input: content

      filters:
        marked: marked
    )
    $("#id_content").allowTabChar()
    row.each ->
      $(this).resizable handles: $(this).attr("id")
      $(this).height(460)
      return


