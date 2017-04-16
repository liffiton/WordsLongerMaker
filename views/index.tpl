<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="author" content="Mark Liffiton">
    <meta name="description" content="WordsLongerMaker takes your words and makes them longer!">
    <title>WordsLongerMaker</title>
    <!-- Google Fonts -->
    <link rel="stylesheet" href="//fonts.googleapis.com/css?family=Roboto:300,700">
    <!-- CSS Reset -->
    <link rel="stylesheet" href="//cdn.rawgit.com/necolas/normalize.css/master/normalize.css">
    <!-- Milligram CSS minified -->
    <link rel="stylesheet" href="//cdn.rawgit.com/milligram/milligram/master/dist/milligram.min.css">
    <!-- Smaller max-width -->
    <style type="text/css">
.container {
  max-width: 80rem;
}
textarea {
  font-family: Roboto;
  min-height: 9rem;
}
    </style>
  </head>
  <body>
    <div class="container">
      <h1 class="title">WordsLongerMaker</h1>
      <form action="/" method="get">
        <fieldset>
          <label for="text">Text:</label>
          <textarea name="text">{{text}}</textarea>
          <input class="button-primary" type="submit" value="WordsLongerMake">
        </fieldset>
      </form>
      %if longer:
      <form action="/" method="get">
        <input name="text" type="hidden" value="{{longer}}">
        <label>Result:</label>
        <blockquote>
          {{longer}}
        </blockquote>
        <p><b>{{ "%0.1f" % (100*len(longer)/len(text)-100) }}% longer!</b> And you can always try to <input class="button-primary" type="submit" value="WordsLongerMakeMore"></p>
      </form>
      %end
    </div>
  </body>
</html>
