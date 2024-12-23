# Insider API Test 
https://petstore.swagger.io/ pet endpointi kullanılarak CRUD operayonlarının gerçekleştirildiği bir API otomasyon projesidir. Proje POM yapısına uygun olarak yazılmıştır. Bu projede yer alan class ve metodların kullanım amaçları şu şekildedir:
## petsore_page.py
Bu classta senaryolarda ortak olarak kullanılacak olan get,post,put, delete operasyonları tanımlanmıştır.
create_pet
get_pet
update_pet
delete_pet
find_by_status: verilen statüye göre get işlemi yapan metod.Örn:(ör. "available", "pending", "sold")
## test_petstore.py
Bu classta aşağıda belirttiğim positive ve negative CRUD işlemleri gerçekleştirilmiştir.
test_create_pet
test_get_pet:positive case,200 response kodunu kontrol eder.
test_not_get_pet:negative case, 404 response kodunu kontrol eder.
test_find_by_status_positive
test_find_by_status_negative
test_update_pet:Update edilen verilerle eşleşip eşleşmediğini kontrol eder.
test_not_update_pet:Update edip , 500 response kod kontrolü yapar.
test_delete_pet:200 bekler.
test_not_delete_pet:404 bekler.

#Test Sonucu:
![image](https://github.com/user-attachments/assets/b639e774-9be8-4041-851e-2f11d2c1c250)

