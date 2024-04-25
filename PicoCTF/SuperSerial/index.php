
<!DOCTYPE html>
<html>
<head>
<link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<link href="style.css" rel="stylesheet">
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</head>
	<body>
		<div class="container">
			<div class="row">
				<div class="col-sm-9 col-md-7 col-lg-5 mx-auto">
					<div class="card card-signin my-5">
						<div class="card-body">
							<h5 class="card-title text-center">Sign In</h5>
														<form class="form-signin" action="index.php" method="post">
								<div class="form-label-group">
									<input type="text" id="user" name="user" class="form-control" placeholder="Username" required autofocus>
									<label for="user">Username</label>
								</div>

								<div class="form-label-group">
									<input type="password" id="pass" name="pass" class="form-control" placeholder="Password" required>
									<label for="pass">Password</label>
								</div>

								<button class="btn btn-lg btn-primary btn-block text-uppercase" type="submit">Sign in</button>
							</form>
						</div>
					</div>
				</div>
			</div>
		</div>
	</body>
</html>
