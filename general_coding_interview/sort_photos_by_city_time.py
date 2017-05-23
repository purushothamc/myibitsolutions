def sortPhotos(S):
    from collections import defaultdict
    from operator import itemgetter

    photos, mapper = list(), defaultdict(list)
    photos_info = S.split("\n")

    for index, each_photo in enumerate(photos_info):
        each_photo = each_photo.split(",")
        each_photo.append(index)
        photos.append(each_photo)

    photos = sorted(photos, key=itemgetter(1))
    photo_groups, result = list(), list()

    for photo in photos:
        mapper[photo[1]].append(photo)

    for photo_group in mapper:
        photo_group = sorted(mapper[photo_group], key=itemgetter(2))
        photo_groups.append(photo_group)

    for photo_group in photo_groups:
        group_len = len(photo_group)
        for index, each_photo in enumerate(photo_group):
            info_ = each_photo[0].split(".")
            each_photo[0] = each_photo[1].strip() + str(index+1).zfill(len(str(group_len))) + "." + info_[1]

    result = []
    for photo_group in photo_groups:
        result.extend(photo_group)
    result = sorted(result, key=itemgetter(3))

    output  = ""
    for each in result:
        output += each[0] +"\n"
    return output

S = 'photo.jpg, Warsaw, 2013-09-05 14:08:15\njohn.png, London, 2015-06-20 15:13:22\nmyFriends.png, Warsaw, 2013-09-05 14:07:13\nEiffel.jpg, Paris, 2015-07-23 08:03:02\npisatower.jpg, Paris, 2015-07-22 23:59:59\nBOB.jpg, London, 2015-08-05 00:02:03\nnotredame.png, Paris, 2015-09-01 12:00:00\nme.jpg, Warsaw, 2013-09-06 15:40:22\na.png, Warsaw, 2016-02-13 13:33:50\nb.jpg, Warsaw, 2016-01-02 15:12:22\nc.jpg, Warsaw, 2016-01-02 14:34:30\nd.jpg, Warsaw, 2016-01-02 15:15:01\ne.png, Warsaw, 2016-01-02 09:49:09\nf.png, Warsaw, 2016-01-02 10:55:32\ng.jpg, Warsaw, 2016-02-29 22:13:11'
print sortPhotos(S)