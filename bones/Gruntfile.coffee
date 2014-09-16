module.exports = (grunt) ->
  template = @option("template" || 'default')
  static_path = @option("static" || '')
  @initConfig
    watch:
      options:
        livereload: true
      css:
        files: ['templates/'+template+'/scss/*.scss']
        tasks: ['compass']

    compass:
      dist:
        options:
          sassDir: 'templates/'+template+'/scss/'
          cssDir: static_path+'/bones/templates/'+template+'/css/'

  @loadNpmTasks("grunt-contrib-watch")
  @loadNpmTasks("grunt-contrib-compass")
  @registerTask "default", ["watch", "compass"]
