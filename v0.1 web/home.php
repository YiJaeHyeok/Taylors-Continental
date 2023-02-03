<!DOCTYPE html>

<html>
<head>
    <title>My first website</title>
</head>
<body>
        <a href="http://localhost/mongo/index.php">
            <button onclick="doSomething()" style="background-color:#333333;color:#00FF00;border-radius:5px">click me!</button>
        </a>

        <p id="test">Hello</p>

        <script>
            function doSomething(){
                document.getElementById("test").innerHTML = "Goodbye";
            }
        </script>
</body>
</html>
