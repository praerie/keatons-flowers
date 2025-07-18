import flower_generator

def run():
    flower_generator.generate_flower(
        petal_count=55,  # will be overridden if use_fibonacci=True
        petal_length=2.0,
        petal_width=0.4,
        randomness=0.05,
        use_fibonacci=True
    )

if __name__ == "__main__":
    run()
