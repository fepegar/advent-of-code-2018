var voronoi;

function setup() {
  createCanvas(windowWidth, windowHeight);
  voronoi = new Voronoi(input);
  voronoi.draw();
  print(voronoi.getMaxArea());
}
