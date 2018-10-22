function setup() {
	var canvas = createCanvas(600, 140);
	canvas.parent('sketch-holder');
	background(255, 0, 200);
}

function draw() {
	if (mouseIsPressed) {
		fill(0);
	} else {
		fill(255);
	}
	ellipse(mouseX, mouseY, 80, 80);
}
