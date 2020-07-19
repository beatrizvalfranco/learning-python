def distribution():
    balls = int(input())
    bucket_1 = []
    bucket_2 = []
    bucket_3 = []

    for ball in range(balls):
        novo_elemento = ball + 1
        
        bucket_1.append(novo_elemento)     
        bucket_2.append(novo_elemento)
        bucket_3.append(novo_elemento)

        buckets = [bucket_1, bucket_2, bucket_3]

    print("buckets = " + str(buckets))


if __name__ == "__main__":
    distribution()


