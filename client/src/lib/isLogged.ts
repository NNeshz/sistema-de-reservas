import Cookies from 'js-cookie';

export const getServerSideProps = async (context) => {
    const cookie = new Cookies(context.req, context.res)
    const token = cookie.get('token')

    const isAuthenticated = token ? true : false

    return {
        props: {
            isAuthenticated
        }
    }
}