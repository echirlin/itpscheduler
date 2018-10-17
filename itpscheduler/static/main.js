$(function(){
	$from = $('#datepicker-from');
	$to = $('#datepicker-to');

	$from.datepicker({
		numberOfMonths: 3,
	}).on('change', function() {
		$to.datepicker('option', 'minDate', getDate(this));
	});
	$to.datepicker({
		numberOfMonths: 3
	}).on('change', function() {
		$from.datepicker('option', 'maxDate', getDate(this));
	});

	function getDate( element ) {
      var date;
      try {
        date = $.datepicker.parseDate( "mm/dd/yy", element.value );
      } catch( error ) {
        date = null;
      }
 
      return date;
    }
});
