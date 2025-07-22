# Chào bạn nếu bạn đã vào đây thì chúc mừng, trong đây là 1 bảng demo đơn giản về cách ML thuần thúy mà mấy ông già ngày xưa dùng
- ML mà các bạn xem hiện tại chắc chả còn gọi là ML vì cái gì cũng bỏ vào AI và gọi chung là AI, cái gì cũng AI và chả có chút động não nào cho các thuật toán cơ bản
- Ở đây có 1 bảng mô phỏng rất thực tế và đầy đủ với 1 db đơn giản gồm user, user detail và 1 số thứ khác 
=> giải thích đơn giản về ML trong code hiện tại, có nhiều loại ML và trong đây đang dùng dạng thuật toán tăng cường riêng cho từng user và dạng chung cho all user 
 - Ta có: api gợi ý riêng cho từng user id dựa trên product mà họ quan tâm ( thuật toán tăng cường ) -> cái này rất được ưa chuộng và là tiền đề cho các app dạy học, hoặc gợi ý sản phẩm custom riêng cho user, như cách facebook đưa ra đúng cái quản cáo về sản phẩm mà bạn vừa tìm trên google , dạng này sẽ học online mỗi khi có thay đổi từ user ( nên tùy chọn tối ưu vì training online theo thời gian thực sẽ tốn ram, có thể lựa chọn lưu trọng số trong máy người dùng bằng sqllite hay gì đó khá là ok)

 - Ta có: api gợi ý chung, trích xuất từ nhiều user -> có thể dùng cho các bài toán gợi ý sản phẩm trong ngày, theo location, theo xua hướng hoặc gợi ý chung với người trong khu vực và nhiều hơn nữa, đây là cái rất hay để chạy ads giúp tối ưu hóa sản phẩm mà người dùng chung hướng đến , giữ chân khách hàng

 -> về ML, ML = machine learning, máy học nhưng đối với mình thì nó chả khác gì dữ liệu thay đổi và cập nhật lại liên tục nên mình gọi nó là cái mấy ông già ngày xưa dùng, trông là trí tuệ nhân tạo, tự đưa ra quyết định ( cây quyết định ), tính loss ..vv nhưng đối với mình thì cũng chỉ là dữ liệu thay đổi 

 -> luồng cơ bản của Machine learning gốc và cả deep learning -> đưa data training và đáp án , đi qua các thuật toán dự đoán cùng với trọng số ngẫu nhiên -> đưa ra kết quả và so sánh với đán án từ data -> lần đầu 100% sai, sai sẽ trả ra loss, dùng loss để tính lại trọng số để lần tiếp theo đoán sẽ đúng hơn : như việc 1 em bé chơi xếp hình, nếu cảm thấy miếng ghép này k phù hợp với ô này thì sẽ k cho nó vào đó nữa, với data lớn thì việc này sẽ phải lặp lại nhiều lần để có kết quả chính xác, đó là tiền đề cho các AI nhận diện hình ảnh, Yolo, OCR và nhiều cái khác , 
 - Nhưng đa số chỉ khó với data khác ( theo ý mình ) với các data như âm thanh, hình ảnh, thì việc training như vậy sẽ hiệu quả và nặng phần tính loss, phải tinh chỉnh lại 
    -> nhưng với dạng dữ liệu structure , table thì rất đơn giản, đối với tôi nó càng giống so sánh hơn là ML vd ( với bài toán tính toán lộ trình học theo khối ): 
        table điểm, ở đó sẽ có 1k row data về điểm môn học, lộ trình học của 1k user và kết quả cuối cùng, thường nếu dạng thuần thúy không qua ML thì bạn phải xem 1k data đó, rút ra được kết luận đúng từ điểm trung bình, lựa chọn trung bình của từng user để rút ra kết luận chung, sẽ phiền phức ở công thức, việc theo dõi data, đưa ra phán đoán vd: đọc data 10 người, thấy 10 người học thêm toán = diểm toán tăng -> gợi ý học thêm, như vậy sẽ rất mất thời gian, và với ML thì những việc đó hoàng toàn tự động, nên mới gọi là Máy Học

        - vd với data: user 1 -> học toán 9d, học văn 4d, học anh 8d -> lựa chọn học thêm văn -> toán 7, văn tăng 6, anh 7 -> và 1 vài data giống v chỉ là khác nhau về dữ liệu sau đó kết quả cuối cùng -> điểm thi đại học 21 (toán 6 vă 7 anh 8 ) khối D001, và .. bao nhiêu điểm đó khối khác 
        - ML sẽ đọc 1k Data như vậy và đưa 1 file chứa trọng số chung, sau này có người gọi đến mô hình truyền tham số đầu vào(điểm hiện tại, điểm mong ước, khối mong ước) -> AI sẽ tính toán và đưa ra được những hướng đi chính xác, ví dụ theo khối A01 thì k cần học thêm môn này, nếu muốn vô trường này thì phải học thêm môn này, có thể tiêu cực 1 chút là bỏ hẳn 1 môn nào đó, ôn vừa đủ qua môn và tập trung all công lực vào các môn còn lại để tối ưu lộ trình    
        -> đó là ML, nhưng tôi thì thích xem nó như dạng dữ liệu thay đổi hơn 

=> và trong python có thư viện sklearn, đây là cái rất nhiều ông kỹ sư GPT ( những kẻ thiếu kiến thức ) không biết , đa số hiện tại bảo anh hãy phân thích data A với data B thế là họ ném hết vào AI -> ok tốt với data nhỏ, data lớn thì sao ? bị leak dữ liệu thì sao ? 

-> sklearn chứa khá nhiều (hiện tại tôi biết ( biết và hiểu chứ kêu viết công thức thì thua, và với người theo AI/ML cũng k cần hiểu gốc rễ sâu, chỉ cần biết dùng thuật toán nào , cây quyết định, phân cụm, tăng cường, ..vv ) tổng 111 thuật toán và cũng gần như là tất cả rồi), và sklearn nó cũng có đầy đủ, dùng thì đơn giản 

2 bước với ML:
- Bước 1: training -> đọc file AI-RL-TRAINING 
    - 1.1: Clean dữ liệu: bạn sẽ có 1-1k table cho quá trình training , vd: bạn cần data từ user và cũng cần data từ lượt click, lượt xem, lượt mua, chúng rải rác ở nhiều table, bạn phải clean data lại vào đúng 1 bảng và cũng chỉ lấy những cái cần thiết, table để training k nên có những cái k dùng cho training, với file hiện tại tôi training với table UserDetail và chỉ lấy đúng 2 tham số ProductID, Action ( mua hoặc k mua ..vv) từ đó training ra sản phẩm này được mua nhiều nhất để gợi ý , đây chỉ là dơn giản
    - 1.2: Vì sao phải tối ưu vào đúng 1 table và clean dữ liệu ? -> ML là thuật toán, thuật toán thì chỉ làm việc với số và cũng chỉ cố định, s=v/t -> k có thêm tham số thứ 3 vào được, nên phải tối ưu tối đa dữ liệu đầu vào, sẽ thoải mái hơn 1 chút với các thuật toán làm việc với ma trận nhưng sẽ nặng kiến thức giảm ma trận mà vẫn giữ đặc trưng cũng như nhân chia ma trận
    - chạy file training với data bạn đã chọn, sẽ mât 1 khoảng thời gian và nó sẽ tạo ra file chứa trọng số , đây chính là cái mà chúng ta gọi là AI 
- bước 2: File AI-RL: api.py
    2.1: ở đây chúng ta chỉ cần gọi lại mô hình, truyền tham số đầu vào hoặc gọi thằng đến file đó ( nếu là dạng data global)
        -> ML/AI chia ra 2 loại, personalized ( cá nhân user ) & Global ( chung ): vd nhận diện vật thể -> chung, gợi ý , tính toán hướng đi -> riêng cho user : personalized -> lưu db , Global -> lưu file trọng số dùng chung
    2.2: done rồi đấy, gọi đến mô hình là xong
=> gợi ý thêm: file train_personalized.py ở đó cũng giống như bên training kia nhưng sẽ trọng số theo từng user riêng vd vào db theo userid, và tất cả chỉ cần import sklearn để xử lý phần thuật toán rất đơn giản 

-> đây là mô hình deploy dạng batch nhé 

==> ở trên chỉ là đơn giản cho người mới học về ML,AI

- Muốn đi sâu thì phải rõ cả 111 thuật toán để tối ưu, scale lớn khó kiểm xoát, phải biết sai ở đâu để debug, tối ưu đồng bộ hay bất đồng bộ khi lưu trọng số dạng per-user, PyTorch/TF cho custom, Spark ML cho distributed,vector embedding ( RAG)
và phải rõ về pipeline,log, tối ưu luồng để còn đưa vào môi trường production, nếu ok phần trên bạn có thể ở Mid level ( nếu có kiến thức sơ về xây dựng pipeline và debug), còn cơ bản thì vẫn ở junior và ôn 1 chút sẽ lên trình rất nhanh

--> à mà nói về cái vụ ML chỉ là data thay đổi chỉ là nói cho các bạn hiểu ở giai đoạn đầu vì thật sự ML k đơn giản dành cho những cái đó mà dành cho các Data cực lớn không so sánh tay được như ảnh ..vv thì con người k nhúng tay vô được vd:
    - CV:computer vison ( ảnh )
    - NLP: Natural Language Processing: văn bảng, câu chữ tự nhiên như giao tiếp
    - Audio 
    -> data của chúng rất phức tạp và nhiều chiều, văn bảng tiếng anh embedding có thể tới 300+ chiều và tiếng việt có thể lên tới 700+ chiều , ảnh cũng vậy, ta k thể xem từng pixel để so sánh được

=>  ALL thông tin trên chỉ là giải thích cho người chưa hoặc ít kiến thức về AI hiểu, và thật sự đọc xong thì 80% sẽ hiểu rõ bản thân thiếu gì và nên bắt đầu học những gì, chúc bro thành công 

Tui vừa trúng Tech Lead AI ở cty to đùng chà bá luôn Muhahahaha ( Tui viết cái này mà k dùng chatgpt, dùng kiến thức thuần thúy trong lúc brain rot nên sẽ thiếu nhưng tui đảm bảo 100% cái này phù hợp và ok cho ai vừa bắt đầu với AI để hiểu và sử dụng được ) 
-> cách chạy các file, AI-RL-TRAINING / AI-RL
- Tạo máy ảo python: python -m venv venv
- Active máy ảo:  venv\Scripts\activate
- Cài Lib: pip install -r requirements.txt
- AI-RL-TRAINING : chạy python train.py / AI-RL chạy python training_personlazied_gì_đó_ấy .py
- Done ALL: copy paste file trainign từ AI-RL-TRAINING vào AI-RL sau đó mở terminal của AI-RL đã active chạy: uvicorn main:app --host 0.0.0.0 --port 8001 --reload  
-> done : test qua api post man hoặc truy cập localhost:8001/doc# gì đó là ok 
-> lưu ý với all file python muốn làm gì cũng active máy ảo trước còn k thì bạn xóa python là vừa
