cmake_minimum_required(VERSION 3.5)
project(src)
set(CMAKE_CXX_STANDARD 17)

add_executable(can_transmit
    can_transmit.c
)

add_executable(can_receive
    can_receive.c
)

add_executable(can_continuous_tx
    can_continuous_tx.c
)

add_executable(can_continuous_rx
    can_continuous_rx.c
)

add_executable(rx_app
    rx_app.c
)

add_executable(tx_app
    tx_app.c
)

# Libraries
# when running g++ these will be included as -static LIB or -lLIB
# target_link_libraries(${PROJECT_NAME}
#     pthread
# )
