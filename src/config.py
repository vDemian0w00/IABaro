class DevelopmentConfig:
    DEBUG=True
    PORT=4000

class ProductionConfig:
    DEBUG=False
    PORT=5000


config={
    'development':DevelopmentConfig
}