KindEditor.ready(function (K) {
    window.editor = K.create('textarea[id=id_body]', {
        width: '800px',
        height: '200px',
        uploadJson: '/admin/upload/kindeditor'
    });
});