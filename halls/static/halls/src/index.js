let id_display_search = '#search_results'
const callAPI = async (text, callback) => {
    await $.ajax({
        url: '/video/search',
        data: {
            'search_term': text
        },
        dataType: 'json'
    })
    .done(callback)
}

const populateSearchContainer =  (data) => {
    $(id_display_search).text(JSON.stringify(data))
}

$("#id_search_term").keyup(function(){
    let search_text = $(this).val()
    $(id_display_search).text('Loading...')
    callAPI(search_text,populateSearchContainer)
});