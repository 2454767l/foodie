//adapted from Azzopardi, Leif and Maxwell, David. 2020. Tango With Django 2. 
$document.ready(function(){
    $('#upvote_button').click(function(){
        var recipe_id = $(this).attr('data-recipeid');

        $.get('foodie/like_recipe',
            {'recipe_id': recipe_id},
            function(data){
                $('#upvote_header').html(data + "Upvotes");
                $('#upvote_button').hide();
            })
        
    });
});