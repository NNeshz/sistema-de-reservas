
// TODO: Create a function to fetch all the products of this category

import MaxWidthWrapper from "@/components/shared/MaxWidthWrapper"
import DishDetailedCard from "@/components/shared/DishDetailedCard"

const page = () => {
  return (
    <div>
        <MaxWidthWrapper>
            <h2>This are name</h2>
            <section>
                <DishDetailedCard />
            </section>
        </MaxWidthWrapper>
    </div>
  )
}

export default page