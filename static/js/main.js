
particlesJS.load('hero', '/static/js/particles-settings.json')
$('#mySlider').carousel({
  interval: false
})
$('#sam').click(function() {
	$('#rnd_input').toggleClass('invisible');
	$('#sam_input').toggleClass('invisible');
	$('#limits').toggleClass('invisible');
 });
$('#rnd').click(function() {
	$('#rnd_input').toggleClass('invisible');
	$('#sam_input').toggleClass('invisible');
	$('#limits').toggleClass('invisible');
 });


